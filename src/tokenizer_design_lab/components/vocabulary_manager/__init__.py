"""Vocabulary Manager.

Handles the serialization of the vocabulary and merge rules, supporting both loading and saving operations.
"""

from tokenizer_design_lab.components.vocabulary_manager.adapter import ROLE, build
from tokenizer_design_lab.components.vocabulary_manager.config import CONFIG, VocabularyManagerConfig
from tokenizer_design_lab.components.vocabulary_manager.errors import VocabularyManagerError
from tokenizer_design_lab.components.vocabulary_manager.service import VocabularyManagerService

__all__ = ["CONFIG", "ROLE", "build", "VocabularyManagerConfig", "VocabularyManagerError", "VocabularyManagerService"]
