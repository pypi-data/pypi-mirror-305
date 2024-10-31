# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

try:
    from collections import Mapping
except ImportError:
    from collections.abc import Mapping

from .iterable import is_iterable


def tuplize(obj, iterable_exclusions=None):
    """
    Function to convert nested mappings and iterable items into tuples. This was mainly useful for
    python 2.7 to facilitate equality checks for simple dict structures, etc.

    TODO: evaluate if there are still use cases that require this for newer versions of Python.

    :param obj:
    :param iterable_exclusions:
    :return:
    """
    result = []
    if obj is not None:
        if isinstance(obj, Mapping):
            result.append(tuplize(obj.items(), iterable_exclusions))
        elif not is_iterable(obj, excluded_types=iterable_exclusions):
            result.append(((), obj))
        else:
            for o in obj:
                result.extend(tuplize(o, iterable_exclusions))
    return tuple(result)
