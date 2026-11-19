"""Static configuration for the BPE Trainer component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BpeTrainerConfig:
    name: str = "bpe_trainer"
    display_name: str = 'BPE Trainer'
    role: str = "enrich"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Iteratively merges the most frequent pairs of adjacent symbols in the training corpus to build the vocabulary.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = BpeTrainerConfig()
