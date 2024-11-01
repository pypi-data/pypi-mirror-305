import os
import pytest
from pathlib import Path
from configurer.core.loader import (
    load_config,
    ConfigurationError,
    EnvironmentVariableNotFoundError,
    replace_env_variables
)

@pytest.fixture
def env_vars(monkeypatch):
    """Setup environment variables for testing."""
    # Use monkeypatch instead of directly setting os.environ
    monkeypatch.setenv('ENV_VALUE_2', 'test_value_2')
    monkeypatch.setenv('ENV_VALUE_3', 'test_value_3')
    monkeypatch.setenv('NESTED_VAR', 'nested_value')
    yield

@pytest.fixture
def config_file_with_env(tmp_path):
    """Create a temporary config file with environment variables."""
    content = """
key_1: value1
key_2: $ENV_VALUE_2
key_3: ${ENV_VALUE_3}
key_4:
  - a
  - b
  - $NESTED_VAR
"""
    config_file = tmp_path / "config.yaml"
    config_file.write_text(content)
    return config_file

def test_replace_env_variables_simple(monkeypatch):
    """Test replacing environment variables in a simple string."""
    monkeypatch.setenv('TEST_VAR', 'test_value')
    assert replace_env_variables('$TEST_VAR') == 'test_value'

def test_replace_env_variables_braces(monkeypatch):
    """Test replacing environment variables using braces syntax."""
    monkeypatch.setenv('TEST_VAR', 'test_value')
    assert replace_env_variables('${TEST_VAR}') == 'test_value'

def test_replace_env_variables_missing():
    """Test behavior with missing environment variables."""
    with pytest.raises(EnvironmentVariableNotFoundError):
        replace_env_variables('$NONEXISTENT_VAR')

def test_replace_env_variables_in_list(monkeypatch):
    """Test replacing environment variables in a list."""
    monkeypatch.setenv('TEST_VAR', 'test_value')
    result = replace_env_variables(['normal', '$TEST_VAR', '${TEST_VAR}'])
    assert result == ['normal', 'test_value', 'test_value']

def test_replace_env_variables_in_dict(monkeypatch):
    """Test replacing environment variables in a dictionary."""
    monkeypatch.setenv('TEST_VAR', 'test_value')
    result = replace_env_variables({
        'normal': 'value',
        'env': '$TEST_VAR',
        'braces': '${TEST_VAR}'
    })
    assert result == {
        'normal': 'value',
        'env': 'test_value',
        'braces': 'test_value'
    }

def test_load_config_with_env_vars(monkeypatch, config_file_with_env):
    """Test loading configuration with environment variables."""
    monkeypatch.setenv('ENV_VALUE_2', 'test_value_2')
    monkeypatch.setenv('ENV_VALUE_3', 'test_value_3')
    monkeypatch.setenv('NESTED_VAR', 'nested_value')
    config = load_config(config_file_with_env)

    print('config:', config)
    # print all attributes of the config object
    for attr in dir(config):
        print(attr, getattr(config, attr))
    
    assert config.key_1 == 'value1'
    assert config.key_2 == 'test_value_2'
    assert config.key_3 == 'test_value_3'
    assert config.key_4 == ['a', 'b', 'nested_value']

def test_load_config_with_missing_env_var(monkeypatch, config_file_with_env):
    """Test loading configuration with a missing environment variable."""
    monkeypatch.setenv('ENV_VALUE_2', 'test_value_2')
    monkeypatch.setenv('ENV_VALUE_3', 'test_value_3')
    # monkeypatch.setenv('NESTED_VAR', None)
    with pytest.raises(EnvironmentVariableNotFoundError):
        load_config(config_file_with_env)

def test_partial_env_var_replacement(monkeypatch):
    """Test replacing environment variables within larger strings."""
    monkeypatch.setenv('TEST_VAR', 'world')
    result = replace_env_variables('hello_$TEST_VAR')
    assert result == 'hello_world'

def test_multiple_env_vars_in_string(monkeypatch):
    """Test replacing multiple environment variables in a single string."""
    monkeypatch.setenv('VAR1', 'hello')
    monkeypatch.setenv('VAR2', 'world')
    result = replace_env_variables('$VAR1 ${VAR2}!')
    assert result == 'hello world!'