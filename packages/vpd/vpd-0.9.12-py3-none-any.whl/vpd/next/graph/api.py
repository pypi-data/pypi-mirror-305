from __future__ import annotations

from glob import glob
from typing import Iterable, Any
from os import path as osp

from ..util import read_yaml
from .plugin_system import PluginRegistry, ensure_sub_dict, Plugin
from .functions import substitute_references
from .input_object import InputObject as _InputObject
from .complex_queries import object_type_iterator

KEY_RAW_DATA = '__raw__'


# noinspection PyCompatibility
def read_all(path: str, verbose=True, extensions=('yml', 'yaml'), recursive=True, namespaces=True):
    data = {}
    path_base = f'{path}/**' if recursive else path
    for ext in extensions:
        # TODO: catch overwriting?
        data.update(_read_files(glob(f'{path_base}/*.{ext}', recursive=recursive),
                                root_path=path, verbose=verbose, namespaces=namespaces))
    return data


# noinspection PyCompatibility
def _read_files(files: Iterable[str], root_path: str, verbose=True, namespaces=True):
    base_path = osp.abspath(root_path)
    result = {}
    for f in files:
        f = f.replace('\\', '/')  # only matters on windows
        dirname = osp.relpath(osp.abspath(osp.dirname(f)), base_path)
        if dirname == '.':
            dirname = ''
        dirname = dirname.replace('\\', '/')  # only matters on windows
        basename, file_type = osp.splitext(osp.basename(f))
        file_type = file_type[1:]  # strip off leading '.'
        unique_id = '/'.join(([dirname] if dirname else []) + [basename])
        namespace = '/'.join(unique_id.split('/')[:-1]) if namespaces else ''
        if verbose:
            print(
                f'Importing: "{f}" | "{dirname}" | "{basename}" | "{file_type}" | '
                f'uid @ read-time = "{unique_id}" | namespace = "{namespace}"')

        content = read_yaml(f, fail_silently=True)
        if not content:
            if verbose:
                print(f'\tNOTICE: No content to load from: {f}')
                pass
            # TODO: warning/notice/error?
            continue

        # this is basically the raw input data schema, other parsers/sources could provide data in this structure...
        result[unique_id] = {
            'content': content,
            'f': f,
            'dirname': dirname,
            'basename': basename,
            'file_type': file_type,
            'uid': unique_id,
            'ns': namespace,
        }

    return result


def parse_raw_data(model: dict, plugin_registry: PluginRegistry, raw_key=KEY_RAW_DATA):
    r = model[raw_key]
    # pass 1: parse into objects
    for uid, raw_content in r.items():
        for type_name, entries in raw_content['content'].items():
            plugin_registry.parse_batch(type_name, entries, model, raw_content)


def make_dict_model(path: str, plugin_registry: PluginRegistry, verbose=True, namespaces=True, raw_key=KEY_RAW_DATA):
    model = {raw_key: read_all(path, verbose=verbose, namespaces=namespaces)}
    parse_raw_data(model, plugin_registry)
    return model


class ModelWrapper(object):
    def __init__(self, model: dict, plugin_registry: PluginRegistry):
        self._global_model = model
        self._plugin_registry = plugin_registry

    def clear(self):
        model = self._global_model
        pr = self._plugin_registry
        pr.clear_compilation(model)
        model.clear()
        return

    def load_yaml_path(self, path: str, verbose=False, extensions=('yml', 'yaml'), recursive=True, namespaces=True):
        model = self._global_model
        pr = self._plugin_registry
        raw_target = ensure_sub_dict(model, KEY_RAW_DATA)

        raw_data = read_all(path, verbose, extensions, recursive=recursive, namespaces=namespaces)
        raw_target.update(raw_data)

        pr.clear_compilation(model)
        parse_raw_data(model, pr, raw_key=KEY_RAW_DATA)
        return

    # TODO: add function to import a single yaml file?
    # TODO: add function to import a dict directly to a namespace?

    def add_plugin(self, plugin: type[Plugin] | Plugin):
        return self._plugin_registry.add(plugin)

    @property
    def model(self):
        return self._global_model

    @property
    def plugin_registry(self):
        return self._plugin_registry

    def get(self, ref: str, calculate=True, type_name=None) -> Any:
        """
        Fetch
        :param ref:
        :param calculate:
        :param type_name:
        :return:
        """
        pr = self._plugin_registry
        model = self._global_model
        if type_name is not None:
            obj = pr.get_type_plugin(type_name).local_registry_lookup(ref, model, default=None)
            if obj and calculate:
                return obj.calculate()
            return obj
        return substitute_references(ref, self._global_model, self._plugin_registry, src=None, calculate=calculate)

    def export(self, name: str | type[Plugin] | Plugin, *args, auto_add=True, **kwargs):
        plugin = self._plugin_registry.get_export_plugin(name, auto_add=auto_add)
        return plugin.export(self._global_model, *args, **kwargs)

    def get_type_plugin(self, name: str):
        return self._plugin_registry.get_type_plugin(name)

    def get_export_plugin(self, name: str | type[Plugin] | Plugin):
        return self._plugin_registry.get_export_plugin(name)

    def get_input_objects(self, generator=True):
        gen = object_type_iterator(self._global_model, self._plugin_registry, _InputObject)
        if generator:
            return gen
        return dict(gen)


def make_model(existing_model: dict = None, existing_plugin_registry: PluginRegistry = None):
    model = {} if existing_model is None else existing_model
    # TODO: need to either make a deep copy and/or re-establish all plugins if using existing
    pr = PluginRegistry() if existing_plugin_registry is None else existing_plugin_registry
    return ModelWrapper(model, pr)
