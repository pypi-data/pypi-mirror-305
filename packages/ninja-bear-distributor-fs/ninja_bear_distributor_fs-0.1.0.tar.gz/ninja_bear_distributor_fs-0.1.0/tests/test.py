import os
import pathlib
import tempfile
import unittest

from typing import Type
from os.path import join

import yaml

from ninja_bear import (
    DumpInfo,
    GeneratorBase,
    LanguageConfigBase,
    NamingConventionType,
    Orchestrator,
    Plugin,
    PropertyType,
)
from src.ninja_bear_distributor_fs.distributor import Distributor


class ExampleScriptGenerator(GeneratorBase):
    """
    ExampleScript specific generator. For more information about the generator methods, refer to GeneratorBase.
    """

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _line_comment(self, string: str) -> str:
        return f'-- {string}'
    
    def _dump(self, info: DumpInfo) -> str:
        code = f'struct {info.type_name}:\n'

        for property in info.properties:
            type = property.type
            value = property.value

            if type == PropertyType.BOOL:
                type_string = 'boolean'
                value = 'true' if value else 'false'
            elif type == PropertyType.INT:
                type_string = 'int'
            elif type == PropertyType.FLOAT:
                type_string = 'float'
            elif type == PropertyType.DOUBLE:
                type_string = 'double'
            elif type == PropertyType.STRING:
                type_string = 'string'
                value = f'\'{value}\''
            elif type == PropertyType.REGEX:
                type_string = 'regex'
                value = f'/{value}/'

            comment = f' {self._line_comment(property.comment)}' if property.comment else ''
            code += f'{" " * info.indent}{type_string} {property.name} = {value}{comment}\n'

        return code


class ExampleScriptConfig(LanguageConfigBase):
    """
    ExampleScript specific config. For more information about the config methods, refer to LanguageConfigBase.
    """

    def _file_extension(self) -> str:
        return 'es'

    def _generator_type(self) -> Type[ExampleScriptGenerator]:
        return ExampleScriptGenerator
    
    def _default_file_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.KEBAP_CASE

    def _allowed_file_name_pattern(self) -> str:
        return r'.+'


class Test(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._config_name = 'test-config'
        self._config_file = f'{self._config_name}.yaml'
        self._test_path = pathlib.Path(__file__).parent.resolve()
        self._test_config_path = join(self._test_path, '..', f'example/{self._config_file}')
        self._plugins = [
            Plugin('examplescript', ExampleScriptConfig),
            Plugin('ninja-bear-distributor-fs', Distributor)
        ]

    def test_distribution(self):
        # Load test-config.yaml directly in test file to allow implementer to modify properties if required.
        with open(self._test_config_path, 'r') as f:
            config = yaml.safe_load(f)

            # Create temp directory and write test config to it.
            with tempfile.TemporaryDirectory() as temp_dir:
                # Update config.
                config['distributors'][0]['paths'] = temp_dir

                orchestrator = Orchestrator.parse_config(config, self._test_config_path, plugins=self._plugins)
                orchestrator.distribute()

                file_exists = os.path.exists(join(temp_dir, f'{self._config_name}.es'))
                self.assertEqual(file_exists, True)
