"""Port and registry adapter for Encoder/Decoder.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from tokenizer_design_lab.components.encoder_decoder.config import CONFIG
from tokenizer_design_lab.components.encoder_decoder.service import EncoderDecoderService
from tokenizer_design_lab.domain.models import PipelineContext

ROLE = CONFIG.role


class EncoderDecoderPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> EncoderDecoderService:
    return EncoderDecoderService(services)
