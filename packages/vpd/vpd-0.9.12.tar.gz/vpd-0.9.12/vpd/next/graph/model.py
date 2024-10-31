from __future__ import annotations
from typing import Any

_no_match = object()


# noinspection PyUnusedLocal
def none_provider(*args, **kwargs):
    return None


class TypeObject(object):
    _raw_ = None  # type: dict
    _obj_ = None  # type: dict
    _global_model_ = None  # type: dict
    _plugin_ = None  # type: "Plugin"

    def __init__(self, obj: dict, global_model: dict, raw: dict):
        self._raw_ = raw
        self._obj_ = obj
        self._global_model_ = global_model

    @property
    def _source_ref(self):
        return self._raw_['f']

    @property
    def uid(self):
        return self._obj_['uid']

    @property
    def namespace(self):
        return self._raw_['ns']

    @property
    def _raw_content(self):
        return self._raw_['content']

    @property
    def _local_plugin_data(self):
        return self._plugin_.local_plugin_data(self._global_model_)

    # noinspection PyProtectedMember
    def calculate(self, target_attribute=None, *args, caller: TypeObject = None, **kwargs):
        plugin = self._plugin_
        model = self._global_model_
        if not plugin.is_compiled(model):
            plugin._registry_.compile(plugin.name, model)

        # TODO: any lookups, calcs, or other stuff required?
        if target_attribute:
            return self._get_calc_value(caller, target_attribute, *args, **kwargs)
        return self._default_output_value(caller, *args, **kwargs)

    # noinspection PyProtectedMember
    def _get_calc_value(self, caller: TypeObject, target_attribute: str, *args, **kwargs):
        """
        Domain-specific implementation of how to take an attribute and return a value
        for it. The default implementation is to use the attribute to get an attribute
        from the object, which can work in many cases--but depending on the use
        context, it may make sense to customize how the target_attribute --> fn mapping
        works.

        :param caller:
        :param target_attribute:
        :param args:
        :param kwargs:
        :return:
        """
        attr = getattr(self, target_attribute, None)
        if callable(attr):
            return attr(caller, *args, **kwargs)
        elif attr is not None:
            return attr  # TODO: any lookups, calcs, or other stuff required?

        return None

    def _default_output_value(self, caller: TypeObject, *args, **kwargs) -> Any:
        """ If a calculation operation gets us to this IRObject, then the result of this property is provided """
        return self

    def _dict(self, caller: TypeObject):
        result = {}
        for k in dir(self):
            if k.startswith('_') or k in ('calculate', 'namespace', 'uid',):
                continue
            v = getattr(self, k)
            if callable(v):
                # try as single-arg function with caller as arg
                # noinspection PyBroadException
                try:
                    result[k] = v(caller)
                    continue
                except:
                    pass
                # try as no-arg function
                # noinspection PyBroadException
                try:
                    result[k] = v()
                    continue
                except:
                    pass
            else:
                result[k] = v
        return result
        # return {k: getattr(self, k) for k in dir(self) if not k.startswith('_')}

    def _object(self, caller: TypeObject):
        return self

    def _get_value(self, *item_aliases, default=None):
        content = self._obj_
        _nm = _no_match  # drag this into local space w/o allocating new object
        for alias in item_aliases:
            result = content.get(alias, _nm)
            if result is not _nm:
                return result
        return default
