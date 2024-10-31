from typing import List
from ninja_bear import GeneratorBase, Property, PropertyType, NamingConventionType, DumpInfo
from ninja_bear.base.generator_configuration import GeneratorConfiguration
from ninja_bear.helpers.package_handling import evaluate_package


class Generator(GeneratorBase):
    """
    Java specific generator. For more information about the generator methods, refer to GeneratorBase.
    """
    def __init__(self, config: GeneratorConfiguration, properties: List[Property] = ..., additional_props=...):
        super().__init__(config, properties, additional_props)

        # Evaluate the config's package name.
        self.package = evaluate_package(
            r'^[a-z][a-z0-9_]+(\.[a-z0-9_]+)*$',
            'See also https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html',
            **self._additional_props,
        )

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _line_comment(self, string: str) -> str:
        return f'// {string}'
    
    def _dump(self, info: DumpInfo) -> str:
        # Add package name.
        code = f'package {self.package};\n\n'

        # Start class definition.
        code += f'public class {info.type_name} {{\n'

        # Add properties.
        for property in info.properties:
            type = property.type

            if type == PropertyType.BOOL:
                type = 'boolean'
                value = 'true' if property.value else 'false'
            elif type == PropertyType.INT:
                type = 'int'
                value = property.value
            elif type == PropertyType.FLOAT:
                type = 'float'
                value = f'{property.value}f'
            elif type == PropertyType.DOUBLE:
                type = 'double'
                value = f'{property.value}d'
            elif type == PropertyType.STRING or type == PropertyType.REGEX:
                type = 'String'
                value = property.value.replace('\\', '\\\\')  # TODO: Might need to be refined.
                value = f'"{value}"'  # Wrap in quotes.
            else:
                raise Exception('Unknown type')
            
            comment = f' {self._line_comment(property.comment)}' if property.comment else ''
            code += f'{" " * info.indent}public final static {type} {property.name} = {value};{comment}\n'

        return code + '}'
