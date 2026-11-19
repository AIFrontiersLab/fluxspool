"""Vocabulary Manager service.

Role: ``enrich``. Annotates candidates with structural features and collapses exact duplicates.

Responsibility (from the architecture specification):
    Handles the serialization of the vocabulary and merge rules, supporting both loading and saving operations.

The service specialises :class:`EnrichStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from tokenizer_design_lab.components.vocabulary_manager.config import CONFIG, VocabularyManagerConfig
from tokenizer_design_lab.components.vocabulary_manager.models import VocabularyManagerInput, VocabularyManagerReport
from tokenizer_design_lab.components.vocabulary_manager.validators import validate_input, validate_output
from tokenizer_design_lab.stages.enrich import EnrichStage

METRIC_PREFIX = "component_vocabulary_manager"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: VocabularyManagerReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class VocabularyManagerService(EnrichStage):
    def __init__(self, services, config: VocabularyManagerConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = VocabularyManagerInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = VocabularyManagerReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = VocabularyManagerReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
