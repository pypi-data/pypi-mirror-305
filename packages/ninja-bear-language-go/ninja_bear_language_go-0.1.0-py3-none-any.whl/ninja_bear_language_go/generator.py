from typing import Callable, List
from ninja_bear import GeneratorBase, Property, PropertyType, NamingConventionType, DumpInfo
from ninja_bear.base.generator_configuration import GeneratorConfiguration
from ninja_bear.helpers.package_handling import evaluate_package


class Generator(GeneratorBase):
    """
    Go specific generator. For more information about the generator methods, refer to GeneratorBase.
    """
    def __init__(self, config: GeneratorConfiguration, properties: List[Property] = ..., additional_props=...):
        super().__init__(config, properties, additional_props)

        # Evaluate the config's package name.
        self.package = evaluate_package(
            r'^[a-z][a-z0-9]+$',
            'See also https://go.dev/doc/effective_go#package-names',
            **self._additional_props,
        )

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _line_comment(self, string: str) -> str:
        return f'// {string}'
    
    def _dump(self, info: DumpInfo) -> str:
        properties = info.properties
        indent = info.indent

        # Set package name.
        code = f'package {self.package}\n\n'

        # Start type definition.
        code += f'var {info.type_name} = struct {{\n'

        # Specify fields.
        for property in properties:
            code += self._property_line(self._field, property, indent)
        code += '}{\n'

        # Assign values.
        for property in properties:
            code += self._property_line(self._value, property, indent)
        return code + '}'

    def _property_line(self, callout: Callable[[Property], str], property: Property, indent: int):
        comment = f' {self._line_comment(property.comment)}' if property.comment else ''
        return f'{" " * indent}{callout(property)}{comment}\n'
    
    def _field(self, property: Property) -> str:
        type = property.type

        if type == PropertyType.BOOL:
            type = 'bool'
        elif type == PropertyType.INT:
            type = 'int'
        elif type == PropertyType.FLOAT or type == PropertyType.DOUBLE:
            type = 'float64'
        elif type == PropertyType.STRING or type == PropertyType.REGEX:
            type = 'string'
        else:
            raise Exception('Unknown type')
            
        REMAINING_SPACE_LENGTH = self._evaluate_longest_property() - len(property.name)
        return f'{property.name}{" " * REMAINING_SPACE_LENGTH} {type}'
    
    def _value(self, property: Property) -> str:
        type = property.type

        if type == PropertyType.BOOL:
            value = 'true' if property.value else 'false'
        elif type == PropertyType.INT:
            value = property.value
        elif type == PropertyType.FLOAT or type == PropertyType.DOUBLE:
            value = property.value
        elif type == PropertyType.STRING or type == PropertyType.REGEX:
            value = property.value.replace('\\', '\\\\')  # TODO: Might need to be refined.
            value = f'"{value}"'  # Wrap in quotes.
        else:
            raise Exception('Unknown type')
            
        REMAINING_SPACE_LENGTH = self._evaluate_longest_property() - len(property.name)
        return f'{property.name}:{" " * REMAINING_SPACE_LENGTH} {value},'
    
    def _evaluate_longest_property(self) -> int:
        """
        Evaluates the length of the name of the property with the longest name.

        :return: Longest property name length.
        :rtype:  int
        """
        longest = 0

        for property in self._properties:
            length = len(property.name)

            if length > longest:
                longest = length
        return longest
