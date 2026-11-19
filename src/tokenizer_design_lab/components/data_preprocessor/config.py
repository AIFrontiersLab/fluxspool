"""Static configuration for the Data Preprocessor component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DataPreprocessorConfig:
    name: str = "data_preprocessor"
    display_name: str = 'Data Preprocessor'
    role: str = "ingest"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Cleans and normalizes domain-specific text to ensure consistent character encoding.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = True
    enforce_sorted_output: bool = False


CONFIG = DataPreprocessorConfig()
