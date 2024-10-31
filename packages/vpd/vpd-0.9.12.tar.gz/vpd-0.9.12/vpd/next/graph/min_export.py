from .plugin_system import ExportPlugin
from .complex_queries import typed_registries_iterator
from .functions import substitute_references
from .model import TypeObject

TYPE_REGISTRY_DICT_EXPORT_PLUGIN_NAME = 'type_registry_dict_export'
OBJECT_EXPORT_PLUGIN_NAME = 'object_export'


class TypeRegistryDictDumpExportPlugin(ExportPlugin):

    @property
    def name(self) -> str:
        return TYPE_REGISTRY_DICT_EXPORT_PLUGIN_NAME

    @property
    def aliases(self) -> list[str]:
        return []

    def export(self, global_model: dict, *args, **kwargs):
        if len(args) < 1:
            raise ValueError('first arg is target_types and must be defined')
        target_types = args[0]
        if isinstance(target_types, str):
            target_types = [target_types]
        target_attrib = args[1] if len(args) > 1 else None

        result = {}
        for uid, obj in typed_registries_iterator(global_model, self._registry_, included_plugins=target_types):
            # desc = extended_get_value(obj, 'description', default=uid)
            # if desc != uid:
            #     desc = f'{desc} [{uid}]'
            value = obj.calculate(target_attribute=target_attrib)
            result[uid] = value

        return result


class ObjectExportPlugin(ExportPlugin):

    @property
    def name(self) -> str:
        return OBJECT_EXPORT_PLUGIN_NAME

    @property
    def aliases(self) -> list[str]:
        return []

    def export(self, global_model: dict, *args, **kwargs):
        pr = self._registry_
        ref = args[0]
        mode = kwargs.pop('mode', 'dict')
        type_name = kwargs.pop('name', None)

        if type_name is not None:
            obj = pr.get_type_plugin(type_name).local_registry_lookup(ref, global_model)
        else:
            obj = substitute_references(ref, global_model, pr, calculate=False)

        if not isinstance(obj, TypeObject):
            return None

        # TODO: if iterable of objects, then apply function to subordinate objects and return list

        if mode == 'dict':
            result = {
                'calculate': obj.calculate(),
            }
            result.update(obj.calculate('_dict'))
            return result

        elif mode == 'object':
            return obj

        raise ValueError(f'mode "{mode}" not recognized')

        pass
