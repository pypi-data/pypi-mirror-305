# noinspection PyUnresolvedReferences
from ..legacy.cid import CaseInsensitiveDict
# noinspection PyUnresolvedReferences
from ..legacy.iterable import flatten, is_iterable

from os import path as osp, makedirs

import yaml
from io import StringIO
from six import string_types


def open_ensure_paths(file_target, mode, *args, force_extension=None, **kwargs):
    if force_extension and not file_target.endswith(force_extension):
        file_target += force_extension

    makedirs(osp.dirname(file_target), exist_ok=True)
    return open(file_target, mode, *args, **kwargs)


def _read_yaml(src, fail_silently=False):
    try:
        with open(src, 'r') as f:
            content = yaml.safe_load(f)
        return content
    except (IOError, OSError) as e:
        if fail_silently:
            return {}
        raise e


def read_yaml(path, origin=None, return_path=False, windows_pseudo_links=False, fail_silently=False):
    """
    Extended function to read yaml files and potentially augment the source path relative to another path and/or return the path

    :param path:
    :param origin:
    :param return_path: whether to return the path
    :param windows_pseudo_links: whether to try to follow text files that contain an alternative path (i.e. fake symlinks for windows).
            Note that in previous versions, `windows_pseudo_links` was True by default since that was the most convenient functionality for
            cross-platform development; however, the default has since changed to False... to avoid any possible security concerns that
            could come from trying to open additional files as a result of the request.
    :param fail_silently: return an empty dict if unable to read data from the file for typical I/O reasons (file not found, etc.)
    :return:
    """
    # TODO: based on whether the provided path and origin are abs/rel, there needs to be more logic if this should be universally applicable
    if not origin:
        path = osp.abspath(path)
    else:
        path = osp.abspath(osp.join(origin, path))

    data = _read_yaml(path, fail_silently=fail_silently)
    path = osp.dirname(path)

    # Windows symlink checking--if file content is just a string and can evaluate to a path when combined with the
    # file origin/path--then that means we're likely looking at a fake symlink style thing... and we should try following it
    if windows_pseudo_links and isinstance(data, string_types):
        try:
            # note that as written/implemented, this really only works for relative paths in fake symlinks...
            dp2 = read_yaml(data, path, return_path=True, windows_pseudo_links=True, fail_silently=fail_silently)
            data, path = dp2
        except (IOError, OSError):
            pass

    if not return_path:
        return data
    return data, path


def parse_yaml(src: str):
    """
    Convenience function to parse yaml files.

    :param src: source text to parse
    :return: yaml parse result
    """
    return yaml.safe_load(StringIO(src))
