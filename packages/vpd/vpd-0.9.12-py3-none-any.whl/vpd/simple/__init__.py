from typing import Iterable, Any

_no_match = object()


def search_tree(sources: Iterable, key: str, default: Any = None):
    """
    Search for a matching key in an ordered iterable of dict objects

    :param sources: ordered iterable of dict objects (or technically any objects that implement __getitem__ and __contains__)
    :param key: the key to search for in the dicts
    :param default: default object to return if nothing is found, if default is an instance of an exception (e.g. ValueError) then the
    exception is raised
    :return: matching object, default object, or raises exception if default is an Exception
    """
    match = _no_match

    for source in sources:
        if key in source:
            match = source[key]
            break

    if match is not _no_match:
        return match

    if isinstance(default, Exception):
        raise default

    return default
