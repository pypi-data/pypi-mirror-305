from dataclasses import dataclass
from pathlib import Path
from typing import Any, Type, TypeVar, get_type_hints
import yaml
from typing import List

T = TypeVar('T')

class ConfigurationError(Exception):
    """Base exception for configuration related errors."""
    pass

def create_config_class(yaml_data: dict) -> Type:
    """
    Dynamically creates a dataclass based on YAML structure.
    
    Args:
        yaml_data (dict): The parsed YAML data
        
    Returns:
        Type: A dynamically created dataclass type
    """
    # Analyze the YAML structure and create type annotations
    annotations = {}
    for key, value in yaml_data.items():
        if isinstance(value, list):
            annotations[key] = List[Any]
        else:
            annotations[key] = Any
            
    # Create the dataclass
    @dataclass
    class DynamicConfig:
        pass
    
    # Add the type hints
    for key, type_hint in annotations.items():
        setattr(DynamicConfig, '__annotations__', annotations)
        setattr(DynamicConfig, key, yaml_data.get(key))
        
    return DynamicConfig

def load_config(config_path: str | Path) -> Any:
    """
    Loads configuration from a YAML file and returns a typed dataclass.
    
    Args:
        config_path: Path to the YAML configuration file
        
    Returns:
        An instance of the dynamically created configuration class
        
    Raises:
        ConfigurationError: If the file cannot be read or parsed
    """
    try:
        # Read and parse YAML file
        with open(config_path, 'r') as f:
            yaml_data = yaml.safe_load(f)
            
        if not isinstance(yaml_data, dict):
            raise ConfigurationError("Root YAML structure must be a dictionary")
            
        # Create the configuration class
        ConfigClass = create_config_class(yaml_data)
        
        # Create an instance with the YAML data
        return ConfigClass()
        
    except yaml.YAMLError as e:
        raise ConfigurationError(f"Error parsing YAML: {e}")
    except IOError as e:
        raise ConfigurationError(f"Error reading configuration file: {e}")
    except Exception as e:
        raise ConfigurationError(f"Unexpected error loading configuration: {e}")

# Example usage
if __name__ == "__main__":
    # Example configuration content
    example_config = """
key_1: value1
key_2: value2
key_3:
  - a
  - b
"""
    
    # Save example config to a temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as temp:
        temp.write(example_config)
        temp_path = temp.name
    
    try:
        # Load the configuration
        config = load_config(temp_path)
        
        # Demonstrate usage
        print(f"Configuration loaded successfully:")
        print(f"key_1: {config.key_1}")
        print(f"key_2: {config.key_2}")
        print(f"key_3: {config.key_3}")
        
        # Show that it's properly typed
        print("\nType annotations:")
        print(get_type_hints(config.__class__))
        
    finally:
        # Clean up temporary file
        Path(temp_path).unlink()