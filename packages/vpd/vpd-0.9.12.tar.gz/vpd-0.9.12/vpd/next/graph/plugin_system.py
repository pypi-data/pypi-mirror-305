from __future__ import annotations

from copy import copy

from .model import TypeObject


def ensure_sub_dict(top: dict, name: str) -> dict:
    if name not in top:
        result = top[name] = {}
    else:
        result = top[name]
    return result


class Plugin(object):
    _registry_ = None  # type: PluginRegistry  # plugins can only be attached to a single registry at a time

    @property
    def name(self) -> str:
        raise NotImplementedError('not implemented')

    @property
    def type_definition(self) -> type[TypeObject]:
        raise NotImplementedError('not implemented')

    @property
    def aliases(self) -> list[str]:
        return []

    @property
    def all_names(self):
        return sorted(set([self.name] + self.aliases))

    def parse_delegate(self, type_name: str, entries: dict | list, global_model: dict, raw_content: dict, **kwargs):
        return self._registry_.parse_batch(type_name, entries, global_model, raw_content, **kwargs)

    def parse(self, obj: dict, local_registry: dict, global_model: dict, raw_content: dict, **kwargs) -> TypeObject:
        raise NotImplementedError('parse function must be implemented')

    def compile(self, local_registry: dict, local_plugin_data: dict, global_model: dict, **kwargs):
        return

    def is_compiled(self, global_model: dict):
        return self.local_plugin_data(global_model).get('_compiled_', False)

    def set_compiled_flag(self, global_model: dict, value: bool = True):
        self.local_plugin_data(global_model)['_compiled_'] = value

    def local_model_registry(self, global_model: dict):
        local_registry = ensure_sub_dict(global_model, self.name)
        return local_registry

    def local_registry_lookup(self, uid: str, global_model: dict, default=None):
        return self.local_model_registry(global_model).get(uid, default)

    def local_registry_items(self, global_model: dict):
        return self.local_model_registry(global_model).items()

    def local_plugin_data(self, global_model: dict):
        plugin_data = ensure_sub_dict(global_model, '__type_plugin_data')
        local_plugin_data = ensure_sub_dict(plugin_data, self.name)
        return local_plugin_data

    pass


# noinspection PyAbstractClass
class ExportPlugin(Plugin):

    @property
    def type_definition(self):
        return None

    def local_plugin_data(self, global_model: dict):
        plugin_data = ensure_sub_dict(global_model, '__export_plugin_data')
        local_plugin_data = ensure_sub_dict(plugin_data, self.name)
        return local_plugin_data

    def parse(self, obj: dict, local_registry: dict, global_model: dict, raw_content: dict, **kwargs) -> TypeObject:
        raise TypeError('parse should not be called for export plugins')

    def export(self, global_model: dict, *args, **kwargs):
        raise NotImplementedError('export must be defined per export plugin')


class MinimalPlugin(Plugin):
    # noinspection PyDefaultArgument
    def __init__(self, type_name: str, ir_type: type[TypeObject] = TypeObject, type_aliases: list[str] = []):
        self._type_name = type_name
        self._type = ir_type
        self._type_aliases = type_aliases

    @property
    def name(self) -> str:
        return self._type_name

    @property
    def type_definition(self) -> type[TypeObject]:
        return self._type

    @property
    def aliases(self) -> list[str]:
        return self._type_aliases

    def parse(self, obj: dict, local_registry: dict, global_model: dict, raw_content: dict, **kwargs) -> TypeObject:
        return self._type(obj, global_model, raw_content)


def _get_plugin_instance(plugin: type[Plugin] | Plugin, shallow_copy=True):
    if isinstance(plugin, Plugin):
        instance = copy(plugin) if shallow_copy else plugin
    elif issubclass(plugin, Plugin):
        instance = plugin()  # fresh instance for registry, no copy required
    else:
        raise ValueError('plugin must be either a subclass or instance of Plugin')
    return instance


class PluginRegistry(object):
    def __init__(self):
        self._type_registry = {}  # type: dict[str, Plugin]
        self._export_registry = {}  # type: dict [str, ExportPlugin]
        self._types_mapping = {}  # type: dict[str, list[str]]  # mapping of type name (so hashable) to TypePlugin.name

    def add(self, plugin: type[Plugin] | Plugin):
        instance = _get_plugin_instance(plugin, shallow_copy=True)
        is_export_plugin = isinstance(instance, ExportPlugin)

        registry = self._type_registry if not is_export_plugin else self._export_registry
        instance._registry_ = self  # assign registry instance (note: means can't re-use plugins)
        types = instance.all_names
        for t in types:
            registry[t] = instance

        # register type mapping information
        types_map = self._types_mapping
        plugin_type = instance.type_definition
        pt_name = plugin_type.__name__
        if pt_name in types_map:
            types_map[pt_name].append(instance.name)
        else:
            types_map[pt_name] = [instance.name]

        return

    # noinspection DuplicatedCode
    def normalize_type_name(self, name: str | Plugin | type[Plugin], auto_add=True):
        plugin = None
        if not isinstance(name, str):
            plugin = _get_plugin_instance(name, shallow_copy=False)
            name = plugin.name

        registry = self._type_registry
        if name not in registry and auto_add and plugin:
            # note may double-instantiate new plugins, probably not worth doing anything about...
            self.add(plugin)
        elif name not in registry:
            raise ValueError(f'type plugin name "{name}" not listed as registered plugin')
        return registry[name].name

    # noinspection DuplicatedCode
    def normalize_export_plugin_name(self, name: str | Plugin | type[Plugin], auto_add=True):
        plugin = None
        if not isinstance(name, str):
            plugin = _get_plugin_instance(name, shallow_copy=False)
            name = plugin.name

        registry = self._export_registry
        if name not in registry and auto_add and plugin:
            # note may double-instantiate new plugins, probably not worth doing anything about...
            self.add(plugin)
        elif name not in registry:
            raise ValueError(f'export plugin name "{name}" not listed as registered plugin')
        return registry[name].name

    def parse_batch(self, name: str, entries: dict | list, global_model: dict, raw_content: dict, **kwargs):
        if isinstance(entries, dict):
            return self.parse(name, entries, global_model, raw_content, i=None)
        elif isinstance(entries, list):
            return [self.parse(name, entry, global_model, raw_content, i=i) for i, entry in enumerate(entries)]
        else:
            raise ValueError('invalid input')

    def parse(self, type_name: str, obj: dict, global_model: dict, raw_content: dict, i: None | int, **kwargs):
        if type_name not in self._type_registry:
            raise ValueError(f'type name "{type_name}" not listed as registered plugin')
        plugin = self._type_registry[type_name]
        local_registry = plugin.local_model_registry(global_model)

        # modify UID to act as a lookup-friendly ID
        if 'name' in obj:  # TODO: name aliases (and/or configurable?)
            modified_uid = f"{raw_content['ns']}/{obj['name']}"
        elif i is not None:  # TODO: check if things break when namespaces disabled...
            modified_uid = f"{raw_content['uid']}/{i}"
        else:
            modified_uid = raw_content['uid']

        # raw_content['uid'] = modified_uid
        obj['uid'] = modified_uid

        result = plugin.parse(obj, local_registry, global_model, raw_content, **kwargs)
        result._plugin_ = plugin  # force plugin reference

        # check for duplication issues...
        uid = result.uid  # get UID from object to let downstream parser make changes if needed
        if uid in local_registry:
            raise ValueError(f'duplicate unique ID: "{uid}" for type "{type_name}"')

        local_registry[uid] = result
        return result

    def clear_compilation(self, global_model: dict):
        for (name, plugin) in self._type_registry.items():
            plugin.local_plugin_data(global_model).clear()

    def compile(self, name: str, global_model: dict, **kwargs):
        plugin = self.get_type_plugin(name)
        local_registry = plugin.local_model_registry(global_model)
        local_plugin_data = plugin.local_plugin_data(global_model)

        result = plugin.compile(local_registry, local_plugin_data, global_model, **kwargs)
        plugin.set_compiled_flag(global_model)
        return result

    def export(self, name: str, global_model: dict, *args, **kwargs):
        return self.get_export_plugin(name).export(global_model, *args, **kwargs)

    def get_type_plugin(self, name: str | type[Plugin] | Plugin, auto_add=True):
        name = self.normalize_type_name(name, auto_add=auto_add)
        return self._type_registry[name]

    def get_export_plugin(self, name: str | type[Plugin] | Plugin, auto_add=True):
        name = self.normalize_export_plugin_name(name, auto_add=auto_add)
        return self._export_registry[name]

    def get_plugins_from_type(self, name: str | type[TypeObject]):
        if isinstance(name, type):
            name = name.__name__
        # TODO: more complex handling here?
        return self._types_mapping.get(name, [])

    pass
