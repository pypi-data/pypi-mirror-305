from __future__ import annotations

from copy import copy
from fnmatch import fnmatch
from itertools import chain
from typing import Iterable

from .model import TypeObject
from .functions import extended_get_value
from .plugin_system import PluginRegistry, Plugin

SEARCH_NAMESPACE = 'ns'
SEARCH_EXCLUSIVE = 'exclusive'
SEARCH_EXCLUDES = 'excludes'
SPECIAL_KEYS = (SEARCH_NAMESPACE, SEARCH_EXCLUSIVE, SEARCH_EXCLUDES,)


def flex_dict_iter(src: list | dict):
    if isinstance(src, list):
        for s in src:
            # TODO: make it more flexible w/ recursion, this is single use-case now
            yield from s.items()
    elif isinstance(src, dict):
        yield from src.items()


def typed_registries_iterator(global_model: dict, plugin_registry: PluginRegistry,
                              included_plugins: Iterable[str | Plugin | type[Plugin]] = None,
                              excluded_plugins: Iterable[str | Plugin | type[Plugin]] = None):
    """
    Iterator that will go through all model registry objects, excluding specified types. If
    included_types is specified, then at most, those types will be considered. If included_types
    is not specified (default), then all types minus excluded types will be considered.

    :param global_model:
    :param plugin_registry:
    :param included_plugins:
    :param excluded_plugins:
    :return:
    """
    if included_plugins is not None:
        included_plugins = set(plugin_registry.normalize_type_name(n) for n in included_plugins)
    else:
        # noinspection PyProtectedMember
        included_plugins = set(plugin_registry._type_registry.keys())

    if excluded_plugins is not None:
        included_plugins.difference_update(set(plugin_registry.normalize_type_name(n) for n in excluded_plugins))

    for uid, obj in chain.from_iterable(plugin_registry.get_type_plugin(t).local_registry_items(global_model)
                                        for t in included_plugins):
        yield uid, obj

    pass


def _search_inner(kv_iterable, query_object: dict):
    hits = {}
    for (uid, obj) in kv_iterable:  # type: str, TypeObject
        hit = False

        # look for field matches
        for (qk, qv) in query_object.items():
            if qk in SPECIAL_KEYS or qk.startswith('$'):  # skip special keys
                continue
            ov = extended_get_value(obj, qk)
            if ov == qv or (isinstance(ov, list) and qv in ov):
                hit = True
                break
            elif ov and isinstance(qv, str) and \
                    ('*' in qv or '?' in qv or ('[' in qv and ']' in qv)) and fnmatch(ov, qv):
                hit = True
                break

        # skip if namespace mismatch
        if SEARCH_NAMESPACE in query_object and not fnmatch(obj.namespace, query_object[SEARCH_NAMESPACE]):
            continue
        elif not hit and SEARCH_NAMESPACE in query_object and fnmatch(obj.namespace, query_object[SEARCH_NAMESPACE]):
            hit = True

        if hit:
            # we operate on a query-copy of the object because it may have relevant properties related to the search
            obj = hits[uid] = copy(obj)
            # obj.__dict__ = copy(obj.__dict__)  # TODO: evaluate if we need to do this...
            # attach query_meta to a copy of obj to pass through
            obj._query_meta = query_object
    return hits


def search_query(caller: TypeObject, query_object: dict,
                 target_types: Iterable[str | Plugin | type[Plugin]] = None,
                 excluded_types: Iterable[str | Plugin | type[Plugin]] = None):
    # noinspection PyProtectedMember
    model = caller._global_model_
    # noinspection PyProtectedMember
    pr = caller._plugin_._registry_

    hits = _search_inner(typed_registries_iterator(model, pr,
                                                   included_plugins=target_types,
                                                   excluded_plugins=excluded_types), query_object)

    exclusive = query_object.get(SEARCH_EXCLUSIVE, None)  # or query_object.get('only', None)
    if exclusive:
        key_set = set(hits.keys())
        # remove anything from hits that doesn't meet exclusive constraints
        for (k, v) in flex_dict_iter(exclusive):
            inner_hits = _search_inner(hits.items(), {k: v})
            key_set.intersection_update(inner_hits.keys())
        hits = {k: v for k, v in hits.items() if k in key_set}

    excludes = query_object.get(SEARCH_EXCLUDES, None)
    if excludes:
        key_set = set(hits.keys())
        # remove anything from hits that doesn't meet excludes constraints
        for (k, v) in flex_dict_iter(excludes):
            inner_hits = _search_inner(hits.items(), {k: v})
            key_set.difference_update(inner_hits.keys())
        hits = {k: v for k, v in hits.items() if k in key_set}

    return hits


def object_type_iterator(global_model: dict, plugin_registry: PluginRegistry, name: str | type[TypeObject]):
    plugins = plugin_registry.get_plugins_from_type(name)
    return typed_registries_iterator(global_model, plugin_registry, included_plugins=plugins)
