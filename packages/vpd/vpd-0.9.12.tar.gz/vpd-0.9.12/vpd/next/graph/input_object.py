from .model import none_provider, TypeObject
from .plugin_system import Plugin
from .functions import extended_get_value


class InputObject(TypeObject):

    # noinspection PyCompatibility
    def __init__(self, obj: dict, global_model: dict, raw: dict, value_provider=none_provider):
        super().__init__(obj, global_model, raw)
        self._value_provider = value_provider

    @property
    def value_provider(self):
        return self._value_provider

    @value_provider.setter
    def value_provider(self, value: callable):
        self._value_provider = value

    @property
    def current_value(self):
        return self._value_provider()

    @current_value.setter
    def current_value(self, value):
        self._value_provider = lambda *args: value

    def _default_output_value(self, caller, *args, **kwargs):
        value = self._value_provider()
        if value is None:
            value = extended_get_value(self, 'default')
        return value


class InputPlugin(Plugin):

    def __init__(self, type_name='inputs'):
        self._name = type_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def type_definition(self) -> type[TypeObject]:
        return InputObject

    def parse(self, obj: dict, local_registry: dict, global_model: dict, raw_content: dict, **kwargs) -> TypeObject:
        # TODO: pull value provider from obj and potentially set it up?
        return InputObject(obj, global_model, raw_content)
