# src/configurer/__init__.py
"""Configuration loader package."""

__version__ = "0.2.0"

from configurer.core.loader import load_config, ConfigurationError

__all__ = ["load_config", "ConfigurationError"]