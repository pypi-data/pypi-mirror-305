from enum import Enum
from typing import List
from ninja_bear import GeneratorBase, Property, PropertyType, NamingConventionType, DumpInfo
from ninja_bear.base.generator_configuration import GeneratorConfiguration


class ExportType(str, Enum):
    ESM = 'esm'
    COMMON_JS = 'common-js'
    NONE = 'none'


class UnknownExportTypeException(Exception):
    def __init__(self, export_type: str):
        super().__init__(f'Unknown export type {export_type}')


class Generator(GeneratorBase):
    """
    JavaScript specific generator. For more information about the generator methods, refer to GeneratorBase.
    """
    _ATTRIBUTE_EXPORT = 'export'

    def __init__(self, config: GeneratorConfiguration, properties: List[Property] = ..., additional_props=...):
        super().__init__(config, properties, additional_props)

        # Evaluate which export type to use.
        self.export_type = self._evaluate_export_type()

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _line_comment(self, string: str) -> str:
        return f'// {string}'
    
    def _dump(self, info: DumpInfo) -> str:
        # Export class only directly if ESM is used.
        code = 'export ' if self.export_type == ExportType.ESM else ''

        # Start type definition.
        code += f'{self._type_start(info.type_name)}\n'

        # Create properties.
        for property in info.properties:
            type = property.type

            if type == PropertyType.BOOL:
                value = 'true' if property.value else 'false'
            elif type == PropertyType.INT or type == PropertyType.FLOAT or type ==  PropertyType.DOUBLE:
                value = property.value
            elif type == PropertyType.STRING:
                value = property.value.replace('\\', '\\\\')  # TODO: Might need to be refined.
                value = f'\'{value}\''  # Wrap in single quotes.
            elif type == PropertyType.REGEX:
                value = f'/{property.value}/'  # Wrap in single quotes.
            else:
                raise Exception('Unknown type')
            
            comment = f' {self._line_comment(property.comment)}' if property.comment else '' 
            code += f'{" " * info.indent}{self._property(property.name, value)}{comment}\n'

        # End type definition.
        code += self._type_end()

        # Add module export only if CommonJS is used.
        return code + (f'\nmodule.exports = {self._type_name}' if self.export_type == ExportType.COMMON_JS else '')

    def _type_start(self, type_name: str):
        return f'class {type_name} {{'
    
    def _property(self, name: str, value: str):
        # Realize JavaScript constant by defining a Getter.
        return f'static get {name}() {{ return {value}; }}'
    
    def _type_end(self) -> str:
        return '}'

    def _evaluate_export_type(self) -> ExportType:
        export_type = ExportType.ESM  # Default to ESM.

        if self._ATTRIBUTE_EXPORT in self._additional_props:
            exception_type_string = self._additional_props[self._ATTRIBUTE_EXPORT]

            if exception_type_string == ExportType.ESM:
                export_type = ExportType.ESM
            elif exception_type_string == ExportType.COMMON_JS:
                export_type = ExportType.COMMON_JS
            elif exception_type_string == ExportType.NONE:
                export_type = ExportType.NONE
            else:
                raise UnknownExportTypeException(exception_type_string)
        return export_type
