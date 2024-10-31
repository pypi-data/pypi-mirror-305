from ninja_bear import GeneratorBase, PropertyType, NamingConventionType, DumpInfo


class Generator(GeneratorBase):
    """
    Python specific generator. For more information about the generator methods, refer to GeneratorBase.
    """

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _line_comment(self, string: str) -> str:
        return f'# {string}'
    
    def _dump(self, info: DumpInfo) -> str:
        # Add dataclass import.
        code = 'from dataclasses import dataclass\n\n'

        # Add dataclass decorator.
        code += '@dataclass(frozen=True)\n'

        # Define class.
        code += f'class {info.type_name}:\n'

        # Add properties to class.
        for property in info.properties:
            type = property.type

            if type == PropertyType.BOOL:
                value = 'True' if property.value else 'False'
            elif type == PropertyType.INT or type == PropertyType.FLOAT or type == PropertyType.DOUBLE:
                value = property.value
            elif type == PropertyType.STRING:
                value = property.value.replace('\\', '\\\\')  # TODO: Might need to be refined.
                value = f'\'{value}\''  # Wrap in single quotes.
            elif type == PropertyType.REGEX:
                value = f'r\'{property.value}\''  # Wrap in single quotes.
            else:
                raise Exception('Unknown type')
            
            comment = f'  {self._line_comment(property.comment)}' if property.comment else ''
            code += f'{" " * info.indent}{property.name} = {value}{comment}\n'
        return code
