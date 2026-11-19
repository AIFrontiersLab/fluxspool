"""Data Preprocessor.

Cleans and normalizes domain-specific text to ensure consistent character encoding.
"""

from tokenizer_design_lab.components.data_preprocessor.adapter import ROLE, build
from tokenizer_design_lab.components.data_preprocessor.config import CONFIG, DataPreprocessorConfig
from tokenizer_design_lab.components.data_preprocessor.errors import DataPreprocessorError
from tokenizer_design_lab.components.data_preprocessor.service import DataPreprocessorService

__all__ = ["CONFIG", "ROLE", "build", "DataPreprocessorConfig", "DataPreprocessorError", "DataPreprocessorService"]
