"""Static configuration for the Vocabulary Manager component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VocabularyManagerConfig:
    name: str = "vocabulary_manager"
    display_name: str = 'Vocabulary Manager'
    role: str = "enrich"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Handles the serialization of the vocabulary and merge rules, supporting both loading and saving operations.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = VocabularyManagerConfig()
