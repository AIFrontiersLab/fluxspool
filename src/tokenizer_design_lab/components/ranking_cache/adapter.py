"""Port and registry adapter for Ranking Cache.

Interface from the architecture specification: ``lookup(key) -> ranking | None``
"""

from __future__ import annotations

from typing import Protocol

from tokenizer_design_lab.components.ranking_cache.config import CONFIG
from tokenizer_design_lab.components.ranking_cache.service import RankingCacheService
from tokenizer_design_lab.domain.models import PipelineContext

ROLE = CONFIG.role


class RankingCachePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> RankingCacheService:
    return RankingCacheService(services)
