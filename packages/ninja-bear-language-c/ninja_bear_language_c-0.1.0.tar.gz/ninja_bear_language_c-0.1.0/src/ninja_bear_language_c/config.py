from typing import Type

from .generator import Generator
from ninja_bear import LanguageConfigBase, NamingConventionType


class Config(LanguageConfigBase):
    """
    C specific config. For more information about the config methods, refer to LanguageConfigBase.
    """

    def _file_extension(self) -> str:
        return 'h'

    def _generator_type(self) -> Type[Generator]:
        return Generator
    
    def _default_file_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.SNAKE_CASE

    def _allowed_file_name_pattern(self) -> str:
        return r'^\w+$'
