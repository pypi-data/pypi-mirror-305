from __future__ import annotations

import re
import math
from typing import Any

from .model import TypeObject, _no_match
from .plugin_system import PluginRegistry

# TODO: pick a style? supporting both leaves open room for weird bugs because they are not entirely mutually exclusive
_arg_style1 = re.compile(r"\{([^\s+-/^*]*)}/+([^\s|:]*):*(\S+)*")
_arg_style2 = re.compile(r"([^\s+-/^*]*):/+([^\s|:]*):*(\S+)*")

_math_scope = {
    '__builtins__': None,
    'abs': abs,
    'sum': sum,
    'max': max,
    'min': min,
    'pow': pow,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
}


# noinspection PyCompatibility
def _fix_percent_numbers(content):
    result = content
    if isinstance(content, str) and (c := content.strip())[-1] == '%':
        try:
            result = float(c[:-1]) * 0.01
        except TypeError:
            pass
    return result


def extended_get_value(ir_object: TypeObject, *item_aliases, default=None):
    """
    Try to get value, automatically do a lookup on the result and do extended number parsing on strings

    :param ir_object:
    :param item_aliases:
    :param default:
    :return:
    """
    # noinspection PyProtectedMember
    result = ir_object._get_value(*item_aliases, default=default)
    # noinspection PyProtectedMember
    result = substitute_references(result, ir_object._global_model_, ir_object._plugin_._registry_, ir_object)
    return result


def _parse_references(query: str) -> list[tuple[str, tuple[str, str, str | None]], ...]:
    """
    Parse references in string into parts suitable for lookups/substitutions.

    style1: {"plugin"}/"namespace/name"[:"property"]  | quotes indicate output strings; brackets indicate optional
    style2: "plugin":"namespace/name"[:"property"]    | quotes indicate output strings; brackets indicate optional

    Note that the results are returned as a list instead of a dict to facilitate interior substitutions; interior
    substitutions should generally be possible as long as the substitution order is in reverse order (would require
    that the query string is parsed again after each substitution); also note that, as implemented, the ordering of
    this list is not preserved properly if both types of arg styles are used within one query string. To facilitate
    interior substitutions would require either fixing that limitation or standardizing on one arg style.

    :param query: string that may or may not contain references in either of the two styles above
    :return: [ (replace-friendly-match-string, (plugin-string, namespace-name-string, property-string|None)), ... ]
    """
    # style1: {plugin}/namespace/name:property  # :property is optional
    # style2: plugin:namespace/name:property    # :property is optional
    # noinspection PyTypeChecker
    return ([(m.string[m.start():m.end()], m.groups()) for m in _arg_style1.finditer(query)] +
            [(m.string[m.start():m.end()], m.groups()) for m in _arg_style2.finditer(query)])


# noinspection PyCompatibility
def _single_ref_match(match, model: dict, plugin_registry: PluginRegistry, src: TypeObject = None, calculate=True):
    txt, (type_name, ref, attrib) = match
    # try:
    plugin = plugin_registry.get_type_plugin(type_name)
    # try straightforward lookup
    obj = plugin.local_registry_lookup(ref, model, default=_no_match)
    if src and obj is _no_match:  # 2nd attempt: try to augment namespace reference
        ref = f'{src.namespace}/{ref}'
        obj = plugin.local_registry_lookup(ref, model, default=_no_match)
    if obj is _no_match:  # give up and just return back txt/input
        return txt, txt
    return txt, (obj.calculate(attrib, caller=src) if calculate else obj)
    #     if ref in target_registry:
    #         obj = target_registry[ref]
    #     elif src and (ref := f'{src.namespace}/{ref}') in target_registry:
    #         obj = target_registry[ref]
    #     else:
    #         return txt, txt
    #     return txt, (obj.calculate(attrib, caller=src) if calculate else obj)
    # except KeyError:
    #     return txt, txt


def substitute_references(query: str, model: dict, plugin_registry: PluginRegistry,
                          src: TypeObject = None, calculate=True) -> Any:
    if isinstance(query, str):
        matches = _parse_references(query)
        result = query
        if len(matches) == 1:
            txt, res = _single_ref_match(matches[0], model, plugin_registry, src, calculate)
            if res != txt and isinstance(res, (str, float, int)):
                # TODO: be able to get filter functions from plugin registry?
                result = result.replace(txt, str(_fix_percent_numbers(res)))
            elif res != txt:
                result = res
        elif len(matches) > 1:
            for m in matches:
                txt, res = _single_ref_match(m, model, plugin_registry, src, calculate)
                if res != txt and isinstance(res, (str, float, int)):
                    # TODO: be able to get filter functions from plugin registry?
                    result = result.replace(txt, str(_fix_percent_numbers(res)))
                elif res != txt:
                    result = res
                # if res is not None:
                #     result = result.replace(txt, str(_fix_percent_numbers(res)))
        else:
            # TODO: be able to get filter functions from plugin registry?
            result = _fix_percent_numbers(result)

        # allow basic statement evaluation via interpreter for result strings (to handle math & type magic)
        if isinstance(result, str):
            # noinspection PyBroadException
            try:
                # TODO: be able to get scope definitions from plugin registry?
                result = eval(result, _math_scope, {})  # TODO: local variables in scope?
            except BaseException as e:
                pass
    else:
        result = query

    return result


def lookup_calc(src: TypeObject, query: str, calculate=True):
    # noinspection PyProtectedMember
    return substitute_references(query, src._global_model_, src._plugin_._registry_, src, calculate=calculate)


# noinspection PyCompatibility
def aggregate_child_objects(caller: TypeObject, result: TypeObject | list[TypeObject] | dict[str, TypeObject]):
    output = []
    # TODO: support for n-depth
    # TODO: cycle / infinite recursion prevention
    if isinstance(result, list):
        for s in result:
            r = lookup_calc(caller, s)
            if isinstance(r, TypeObject):
                output.append(r)
            elif isinstance(r, list) and r and isinstance(r[0], TypeObject):
                output.extend(r)
            elif isinstance(r, dict) and r and isinstance((r2 := list(r.values()))[0], TypeObject):
                output.extend(r2)
            else:
                raise ValueError('reference to IRObject or list of IRObjects expected')
    elif isinstance(result, dict) and result and isinstance((r2 := list(result.values()))[0], TypeObject):
        output.extend(r2)
    elif isinstance(result, TypeObject):
        output.append(result)

    return output
