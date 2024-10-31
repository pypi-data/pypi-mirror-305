from typing import Callable
from ninja_bear import GeneratorBase, Property, PropertyType, NameConverter, NamingConventionType, DumpInfo


class Generator(GeneratorBase):
    """
    C specific generator. For more information about the generator methods, refer to GeneratorBase.
    """

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _line_comment(self, string: str) -> str:
        return f'/* {string} */'
    
    def _dump(self, info: DumpInfo) -> str:
        properties = info.properties
        indent = info.indent

        code = f'#ifndef {self._guard_name()}\n#define {self._guard_name()}\n\n'
        code += 'const struct {\n'

        # Specify fields.
        for property in properties:
            code += self._property_line(self._field, property, indent)
        code += f'}} {info.type_name} = {{\n'

        # Assign values.
        for property in properties:
            code += self._property_line(self._value, property, indent)
        code += f'}};\n\n#endif {self._line_comment(self._guard_name())}'

        return code

    def _property_line(self, callout: Callable[[Property], str], property: Property, indent: int):
        comment = f' {self._line_comment(property.comment)}' if property.comment else ''
        return f'{" " * indent}{callout(property)}{comment}\n'

    def _field(self, property: Property) -> str:
        type = property.type
        after_property_name = ''

        if type == PropertyType.BOOL:
            type = 'unsigned char'
        elif type == PropertyType.INT:
            type = 'int'
        elif type == PropertyType.FLOAT:
            type = 'float'
        elif type == PropertyType.DOUBLE:
            type = 'double'
        elif type == PropertyType.STRING or type == PropertyType.REGEX:
            type = 'char'
            after_property_name = f'[{len(property.value) + 1}]'
        else:
            raise Exception('Unknown type')

        return f'{type} {property.name}{after_property_name};'
    
    def _value(self, property: Property) -> str:
        type = property.type

        if type == PropertyType.BOOL:
            value = '1' if property.value else '0'
        elif type == PropertyType.INT:
            value = property.value
        elif type == PropertyType.FLOAT:
            value = f'{property.value}f'
        elif type == PropertyType.DOUBLE:
            value = property.value
        elif type == PropertyType.STRING or type == PropertyType.REGEX:
            value = property.value.replace('\\', '\\\\')  # TODO: Might need to be refined.
            value = f'"{value}"'  # Wrap in quotes.
        else:
            raise Exception('Unknown type')

        return f'{value},'
    
    def _guard_name(self):
        return f'{NameConverter.convert(self._type_name, NamingConventionType.SCREAMING_SNAKE_CASE)}_H'
