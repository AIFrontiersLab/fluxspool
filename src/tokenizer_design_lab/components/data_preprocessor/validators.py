"""Pre- and post-conditions for Data Preprocessor.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from tokenizer_design_lab.components.data_preprocessor.config import DataPreprocessorConfig
from tokenizer_design_lab.components.data_preprocessor.errors import DataPreprocessorContractViolation
from tokenizer_design_lab.components.data_preprocessor.models import DataPreprocessorInput


def validate_input(ctx, config: DataPreprocessorConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise DataPreprocessorContractViolation(
            "too many candidates for data_preprocessor",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: DataPreprocessorInput, config: DataPreprocessorConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise DataPreprocessorContractViolation("duplicate candidate ids after data_preprocessor")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise DataPreprocessorContractViolation(
                "data_preprocessor introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise DataPreprocessorContractViolation("data_preprocessor produced an unsorted ranking")
