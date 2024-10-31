from os import getenv as _os_getenv
import kubernetes
import json
from ..util import parse_yaml
from base64 import b64decode
from datetime import datetime

_CM_PREFIX = 'cm-'
POD_NAMESPACE = _os_getenv('POD_NAMESPACE', 'default')

# try to load kubernetes credentials and then assign api client
try:
    kubernetes.config.load_incluster_config()
except kubernetes.config.ConfigException:
    kubernetes.config.load_kube_config(_os_getenv('KUBECONFIG'), persist_config=False)

_v1 = kubernetes.client.CoreV1Api()
_dc = kubernetes.dynamic.DynamicClient(_v1.api_client)

client = _v1  # expose client because that could be convenient


def truncate_name(name: str, field_name: str = None, limit=52):
    if name is None:
        return None  # shouldn't happen... maybe throw exception instead?

    if len(name) > limit:
        truncated = name[:limit]
        # last character must be an alphanumeric character
        if not truncated[-1].isalnum():
            truncated = truncated[:-1] + 'x'
        return truncated

    return name


# noinspection PyCompatibility
def apply_yaml_object(body: dict, logger=None, verb='patch', create_on_fail=None, suppress_exceptions=False, timeout=30, **res_get_kwargs):
    api_version = body.get('apiVersion', 'v1')
    kind = body.get('kind', None)
    metadata = body.get('metadata', {})
    name = metadata.get('name', '???')
    namespace = metadata.get('namespace', 'default')
    fn_args = {'body': body, '_request_timeout': timeout}

    # switch out first attempt function depending on what we're trying to accomplish
    if verb == 'patch':
        fn = _dc.patch
        if create_on_fail is None:  # default is to create on fail
            create_on_fail = True
    elif verb == 'replace':
        fn = _dc.replace
        if create_on_fail is None:  # default is to create on fail
            create_on_fail = True
    elif verb == 'delete':
        fn = _dc.delete
        if create_on_fail is None:
            create_on_fail = False  # create on fail makes no sense w/ delete request
    elif verb == 'create':
        fn = _dc.create
        if create_on_fail is None:
            create_on_fail = False  # create on fail makes no sense w/ create as first action anyway
    elif verb == 'get':
        fn = _dc.get
        if create_on_fail is None:
            create_on_fail = False  # create on fail makes no sense for get requests
    else:
        raise ValueError(f'verb {verb} not implemented')

    # get dynamic client resource
    fn_args['resource'] = resource = _dc.resources.get(api_version=api_version, kind=kind, **res_get_kwargs)
    # TODO: if it's not a namespaced resource, maybe we set namespace to None?

    # update fn args and other parameters as needed depending on verb
    if verb in ('delete', 'get',):  # for delete and get, we swap args to just be 'name' and 'namespace'
        fn_args['name'] = name
        fn_args['namespace'] = namespace
        del fn_args['body']

    # apply user-requested action as the first pass, hopefully it just works
    exc = None
    try:
        if logger:
            logger.debug(f"Trying to {verb} {kind}: {namespace}/{name}")
        result = fn(**fn_args)
    except kubernetes.client.ApiException as r:
        result = None
        exc = r

    # split out 404 response (attempt to create instead) so that it won't result in a nested exception
    if exc and exc.status == 404 and create_on_fail:
        if logger:
            logger.debug(f"Item not found, trying to create {kind}: {namespace}/{name}")
        try:
            result = _dc.create(resource, body)
            verb = 'create'  # update verb (for logging purposes) if we ended up using create
        except kubernetes.client.ApiException as r:
            raise r
    elif exc and exc.status == 404 and verb in ('delete', 'get',):
        # it's not exception-worthy if we were instructed to delete an entity, and we can't locate it
        # or if instructed to get one... we'll just return None
        result = None
    elif exc and not suppress_exceptions:
        raise exc

    if logger and (result is not None or verb in ('delete',)):
        logger.info(f'Applied {kind}: "{namespace}/{name}" via {verb}')
    return result


# noinspection PyCompatibility
def trigger_cronjob(cronjob_name, man_suffix='man', namespace=POD_NAMESPACE, do_truncate_name=False):
    """ trigger cronjob manually """
    cronjob = apply_yaml_object({
        'kind': 'CronJob',
        'apiVersion': 'batch/v1',
        'metadata': {
            'name': truncate_name(cronjob_name) if do_truncate_name else cronjob_name,
            'namespace': namespace
        }
    }, verb='get')

    if not cronjob:
        return None

    serialized = cronjob.to_dict()
    annotations = dict(cronjob.spec.jobTemplate.annotations or {})
    annotations["cronjob.kubernetes.io/instantiate"] = 'manual'
    job = {
        'apiVersion': 'batch/v1',
        'kind': 'Job',
        'metadata': {
            # it's OK if we make a stupid long name because it'll be truncated automatically
            'name': truncate_name(f"{cronjob.metadata.name}-{man_suffix}-{datetime.utcnow().timestamp()}", limit=60),
            'namespace': cronjob.metadata.namespace,
            'ownerReferences': [{
                'apiVersion': 'v1',
                'kind': 'CronJob',
                'name': cronjob.metadata.name,
                'uid': cronjob.metadata.uid,
            }],
            'labels': dict(cronjob.spec.jobTemplate.metadata.labels or {}),
            'annotations': annotations,
        },
        # cronjob.spec.jobTemplate.spec
        'spec': serialized.get('spec', {}).get('jobTemplate', {}).get('spec', {}),
    }

    return apply_yaml_object(job)


# noinspection PyCompatibility
class NamespacedDataContainerManager(object):
    _resource_name_prefix = _CM_PREFIX
    _data_field_name_prefix = ''
    _field_read = 'data'  # for configmaps # 'stringData' for secrets
    _parse_read = staticmethod(parse_yaml)
    _field_write = 'data'  # for configmaps # 'stringData' for secrets
    _parse_write = staticmethod(json.dumps)
    _api_version = 'v1'
    _kind = 'ConfigMap'  # 'Secret'
    _resource_name_suffix = ''
    _resource_name_guts = None
    _resource_name_fn = None

    def __init__(self, kind='cm', namespace='default', identity_fn=None, resource_name_prefix=None, resource_name_suffix=None,
                 identity_fn_static_override=None, default_data_field_name_prefix=''):
        self._namespace = namespace

        if identity_fn is None and identity_fn_static_override is None:
            raise ValueError('either the "identity_fn" or "identity_fn_static_override" needs to be defined')
        self._resource_name_fn = identity_fn
        self._resource_name_guts = identity_fn_static_override

        if kind == 'cm':
            self._kind = 'ConfigMap'
            self._resource_name_prefix = _CM_PREFIX if resource_name_prefix is None else resource_name_prefix
            self._data_field_name_prefix = default_data_field_name_prefix
            self._field_read = self._field_write = 'data'
        elif kind == 'secret':
            self._kind = 'Secret'
            self._resource_name_prefix = '' if resource_name_prefix is None else resource_name_prefix
            self._data_field_name_prefix = default_data_field_name_prefix
            self._field_read = 'data'
            self._field_write = 'stringData'

            def b64_parse_decode(content):
                decoded = b64decode(content).decode('utf-8')
                return parse_yaml(decoded)

            self._parse_read = staticmethod(b64_parse_decode)
        else:
            raise ValueError(f'kind "{kind}" not implemented')

        if resource_name_suffix is not None:
            self._resource_name_suffix = resource_name_suffix

        return

    def _template(self, name, labels=None, annotations=None):
        result = {
            'apiVersion': self._api_version,
            'kind': self._kind,
            'metadata': {
                'name': name,
                'namespace': self._namespace,
            }
        }
        # populate labels/annotations if provided; not included otherwise
        if labels:
            result['metadata']['labels'] = labels
        if annotations:
            result['metadata']['annotations'] = annotations
        return result

    def _resource_name(self, resource_name=None, identity=None, prefix=None, suffix=None):
        if resource_name is not None:
            return resource_name
        if prefix is None:  # use default prefix if not provided
            prefix = self._resource_name_prefix
        if identity is None:  # try using default identity if provided
            identity = self._resource_name_guts
        if identity is None:  # if not, then we fall back to ENV-derived identity
            identity = self._resource_name_fn()
        if suffix is None:  # use default suffix if not provided
            suffix = self._resource_name_suffix
        return truncate_name(f'{prefix}{identity}{suffix}')

    def _key_name(self, name, name_prefix=None):
        if name_prefix is None:
            name_prefix = self._data_field_name_prefix
        obj_key = f'{name_prefix}{name}' if name_prefix else name
        return obj_key

    # TODO: evaluate adding memoization / LRU cache for get function (requires a few logistics including invalidation)
    def get(self, name: str = 'data', name_prefix=None, resource_name=None, identity=None, resource_name_prefix=None,
            resource_name_suffix=None, return_raw_api_object=False, parse=True) -> str | int | float | dict | list | tuple | None:
        # establish defaults/variables
        resource_name = self._resource_name(resource_name, identity, prefix=resource_name_prefix, suffix=resource_name_suffix)
        obj_key = self._key_name(name, name_prefix)

        # try to get the requested resource
        raw_result = apply_yaml_object(self._template(resource_name), verb='get')
        if return_raw_api_object:
            return raw_result

        # get the specific data entity
        data = getattr(raw_result, self._field_read, None)
        if data and (result := getattr(data, obj_key, None)):
            parse_fn = self._parse_read
            return parse_fn(result) if parse else result

        return None

    def put(self, content: str | int | float | dict | list | tuple, name: str = 'data', name_prefix=None, resource_name=None,
            identity=None, resource_name_prefix=None, parse=True) -> bool:
        # establish defaults/variables
        resource_name = self._resource_name(resource_name, identity, prefix=resource_name_prefix)
        obj_key = self._key_name(name, name_prefix)

        # try to set the requested resource
        template = self._template(resource_name)
        parse_fn = self._parse_write
        template[self._field_write] = {obj_key: parse_fn(content) if parse else content}
        result = apply_yaml_object(template, verb='patch', create_on_fail=True)

        # return something... try to determine if true?
        return bool(result)

    def update(self, content: dict, name='data', name_prefix=None, resource_name=None, identity=None, resource_name_prefix=None) -> bool:
        parse = True
        existing = self.get(name=name, name_prefix=name_prefix,
                            resource_name=resource_name, identity=identity,
                            resource_name_prefix=resource_name_prefix, parse=parse)
        new_data = existing if parse and existing else {}
        new_data.update(content)
        self.put(content=new_data, name=name, name_prefix=name_prefix,
                 resource_name=resource_name, identity=identity, parse=parse)
        return existing != new_data
