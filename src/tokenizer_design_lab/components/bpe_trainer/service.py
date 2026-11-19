"""BPE Trainer service.

Role: ``enrich``. Annotates candidates with structural features and collapses exact duplicates.

Responsibility (from the architecture specification):
    Iteratively merges the most frequent pairs of adjacent symbols in the training corpus to build the vocabulary.

The service specialises :class:`EnrichStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from tokenizer_design_lab.components.bpe_trainer.config import CONFIG, BpeTrainerConfig
from tokenizer_design_lab.components.bpe_trainer.models import BpeTrainerInput, BpeTrainerReport
from tokenizer_design_lab.components.bpe_trainer.validators import validate_input, validate_output
from tokenizer_design_lab.stages.enrich import EnrichStage

METRIC_PREFIX = "component_bpe_trainer"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: BpeTrainerReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class BpeTrainerService(EnrichStage):
    def __init__(self, services, config: BpeTrainerConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = BpeTrainerInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = BpeTrainerReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = BpeTrainerReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
