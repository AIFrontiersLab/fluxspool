"""Typed configuration: defaults in code, profiles in TOML, overrides from the environment."""

from tokenizer_design_lab.config.loader import load_settings
from tokenizer_design_lab.config.settings import Settings

__all__ = ["Settings", "load_settings"]
