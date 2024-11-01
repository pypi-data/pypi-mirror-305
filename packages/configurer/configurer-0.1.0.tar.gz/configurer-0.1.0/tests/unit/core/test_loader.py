import pytest
from pathlib import Path
import yaml
from typing import List, Any, get_type_hints
from configurer.core.loader import load_config, ConfigurationError, create_config_class

@pytest.fixture
def temp_config_file(tmp_path):
    """Fixture to create a temporary YAML config file."""
    config_content = """
key_1: value1
key_2: value2
key_3:
  - a
  - b
"""
    config_file = tmp_path / "config.yaml"
    config_file.write_text(config_content)
    return config_file

@pytest.fixture
def invalid_yaml_file(tmp_path):
    """Fixture to create an invalid YAML file."""
    invalid_content = """
key_1: value1
  invalid_indent:
- not valid yaml
"""
    config_file = tmp_path / "invalid.yaml"
    config_file.write_text(invalid_content)
    return config_file

def test_load_config_basic(temp_config_file):
    """Test basic configuration loading with valid YAML."""
    config = load_config(temp_config_file)
    
    # Test values are correctly loaded
    assert config.key_1 == "value1"
    assert config.key_2 == "value2"
    assert config.key_3 == ["a", "b"]
    
    # Test type hints are correctly set
    type_hints = get_type_hints(config.__class__)
    assert type_hints["key_1"] == Any
    assert type_hints["key_2"] == Any
    assert type_hints["key_3"] == List[Any]

def test_load_config_with_path_object(temp_config_file):
    """Test loading config with Path object instead of string."""
    config = load_config(Path(temp_config_file))
    assert config.key_1 == "value1"

def test_load_config_file_not_found():
    """Test proper error handling when file doesn't exist."""
    with pytest.raises(ConfigurationError) as exc_info:
        load_config("nonexistent.yaml")
    assert "Error reading configuration file" in str(exc_info.value)

def test_load_config_invalid_yaml(invalid_yaml_file):
    """Test proper error handling with invalid YAML."""
    with pytest.raises(ConfigurationError) as exc_info:
        load_config(invalid_yaml_file)
    assert "Error parsing YAML" in str(exc_info.value)

def test_create_config_class_empty():
    """Test creating config class with empty dict."""
    ConfigClass = create_config_class({})
    config = ConfigClass()
    assert len(get_type_hints(config.__class__)) == 0

def test_create_config_class_types():
    """Test type annotation creation for different value types."""
    yaml_data = {
        "string_value": "test",
        "int_value": 123,
        "list_value": [1, 2, 3],
        "dict_value": {"a": 1},
    }
    
    ConfigClass = create_config_class(yaml_data)
    config = ConfigClass()
    
    type_hints = get_type_hints(config.__class__)
    assert type_hints["string_value"] == Any
    assert type_hints["int_value"] == Any
    assert type_hints["list_value"] == List[Any]
    assert type_hints["dict_value"] == Any

def test_non_dict_yaml():
    """Test proper error handling when YAML root is not a dict."""
    yaml_content = "- just\n- a\n- list"
    config_file = Path("temp.yaml")
    
    try:
        config_file.write_text(yaml_content)
        with pytest.raises(ConfigurationError) as exc_info:
            load_config(config_file)
        assert "Root YAML structure must be a dictionary" in str(exc_info.value)
    finally:
        config_file.unlink(missing_ok=True)

def test_dataclass_immutability():
    """Test that the created dataclass preserves values."""
    yaml_data = {
        "key_1": "value1",
        "key_2": [1, 2, 3]
    }
    
    ConfigClass = create_config_class(yaml_data)
    config = ConfigClass()
    
    assert config.key_1 == "value1"
    assert config.key_2 == [1, 2, 3]