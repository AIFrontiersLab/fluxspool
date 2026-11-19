"""Port and registry adapter for Vocabulary Manager.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from tokenizer_design_lab.components.vocabulary_manager.config import CONFIG
from tokenizer_design_lab.components.vocabulary_manager.service import VocabularyManagerService
from tokenizer_design_lab.domain.models import PipelineContext

ROLE = CONFIG.role


class VocabularyManagerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> VocabularyManagerService:
    return VocabularyManagerService(services)
