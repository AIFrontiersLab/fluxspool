"""Port and registry adapter for BPE Trainer.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from tokenizer_design_lab.components.bpe_trainer.config import CONFIG
from tokenizer_design_lab.components.bpe_trainer.service import BpeTrainerService
from tokenizer_design_lab.domain.models import PipelineContext

ROLE = CONFIG.role


class BpeTrainerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> BpeTrainerService:
    return BpeTrainerService(services)
