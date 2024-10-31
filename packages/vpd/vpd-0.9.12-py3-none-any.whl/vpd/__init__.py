# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

# this is a stub to provide backwards compatibility while transitioning code

from .legacy.arguments import arg_substitute
from .legacy.cid import CaseInsensitiveDict
from .legacy.iterable import flatten, is_iterable
from .legacy.yaml_dict import VirtualPathDictChain, get_data, vpd_chain, vpd_data, vpd_get

from .next.util import read_yaml
