"""Encoder/Decoder service.

Role: ``score``. Blends upstream prior scores with query-aware relevance and reorders candidates.

Responsibility (from the architecture specification):
    Converts raw text strings into integer token IDs and vice-versa, handling special tokens (e.g., , ).

The service specialises :class:`ScoreStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from tokenizer_design_lab.components.encoder_decoder.config import CONFIG, EncoderDecoderConfig
from tokenizer_design_lab.components.encoder_decoder.models import EncoderDecoderInput, EncoderDecoderReport
from tokenizer_design_lab.components.encoder_decoder.validators import validate_input, validate_output
from tokenizer_design_lab.stages.score import ScoreStage

METRIC_PREFIX = "component_encoder_decoder"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: EncoderDecoderReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class EncoderDecoderService(ScoreStage):
    def __init__(self, services, config: EncoderDecoderConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = EncoderDecoderInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = EncoderDecoderReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = EncoderDecoderReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
