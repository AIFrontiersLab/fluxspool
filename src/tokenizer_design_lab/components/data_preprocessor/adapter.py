"""Port and registry adapter for Data Preprocessor.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from tokenizer_design_lab.components.data_preprocessor.config import CONFIG
from tokenizer_design_lab.components.data_preprocessor.service import DataPreprocessorService
from tokenizer_design_lab.domain.models import PipelineContext

ROLE = CONFIG.role


class DataPreprocessorPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> DataPreprocessorService:
    return DataPreprocessorService(services)
