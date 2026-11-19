"""Static configuration for the Encoder/Decoder component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EncoderDecoderConfig:
    name: str = "encoder_decoder"
    display_name: str = 'Encoder/Decoder'
    role: str = "score"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Converts raw text strings into integer token IDs and vice-versa, handling special tokens (e.g., , ).'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = True


CONFIG = EncoderDecoderConfig()
