import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Type, TypeVar, get_type_hints, Dict, Union
import yaml
from typing import List

T = TypeVar('T')

class ConfigurationError(Exception):
    """Base exception for configuration related errors."""
    pass

class EnvironmentVariableNotFoundError(ConfigurationError):
    """Raised when a referenced environment variable is not found."""
    pass

def replace_env_variables(value: Any) -> Any:
    """
    Recursively replaces environment variables in configuration values.
    
    Supports two formats:
    - $VAR_NAME
    - ${VAR_NAME}
    
    Args:
        value: The value to process for environment variables
        
    Returns:
        The processed value with environment variables replaced
        
    Raises:
        EnvironmentVariableNotFoundError: If a referenced environment variable is not found
    """
    if isinstance(value, str):
        # Pattern to match both $VAR and ${VAR} formats
        pattern = r'\$\{([^}]+)\}|\$([A-Za-z_][A-Za-z0-9_]*)'
        
        def replace_match(match):
            # Get the variable name from either ${VAR} or $VAR format
            var_name = match.group(1) or match.group(2)
            env_value = os.environ.get(var_name)
            print('should replace with', env_value)
            
            if env_value is None:
                raise EnvironmentVariableNotFoundError(
                    f"Environment variable '{var_name}' not found"
                )
            return env_value
            
        try:
            return re.sub(pattern, replace_match, value)
        except EnvironmentVariableNotFoundError:
            raise
        except Exception as e:
            raise ConfigurationError(f"Error processing environment variables: {e}")
        
    elif isinstance(value, list):
        return [replace_env_variables(item) for item in value]
    elif isinstance(value, dict):
        return {k: replace_env_variables(v) for k, v in value.items()}
    else:
        return value
    

def create_config_class(yaml_data: dict) -> Type:
    """
    Dynamically creates a dataclass based on YAML structure.
    
    Args:
        yaml_data (dict): The parsed YAML data
        
    Returns:
        Type: A dynamically created dataclass type
    """
    # Process environment variables in the YAML data
    processed_data = replace_env_variables(yaml_data)

    # Analyze the YAML structure and create type annotations
    annotations = {}
    for key, value in processed_data.items():
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
        setattr(DynamicConfig, key, processed_data.get(key))
        
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
    except EnvironmentVariableNotFoundError as e:
        raise
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