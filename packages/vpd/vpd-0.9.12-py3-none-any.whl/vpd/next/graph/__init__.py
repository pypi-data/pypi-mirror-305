# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

# this is a simple "plugin" based system to be able to model arbitrary data with complex interrelationships
# in python. the design basis is for a series of yaml files that can reference "types" defined among each other
# and using appropriate "business logic", it is possible to define various novel combinations/uses of the relationships
# to get the intended result from the "pipeline"/"chain"/something...

from .model import (TypeObject, none_provider)
from .functions import (substitute_references, extended_get_value, lookup_calc)
from .plugin_system import (Plugin, PluginRegistry, MinimalPlugin, ExportPlugin)
from .input_object import InputObject
from .api import (parse_raw_data, read_all, make_model, ModelWrapper)
from .min_export import TypeRegistryDictDumpExportPlugin
