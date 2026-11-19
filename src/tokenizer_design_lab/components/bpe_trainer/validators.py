"""Pre- and post-conditions for BPE Trainer.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from tokenizer_design_lab.components.bpe_trainer.config import BpeTrainerConfig
from tokenizer_design_lab.components.bpe_trainer.errors import BpeTrainerContractViolation
from tokenizer_design_lab.components.bpe_trainer.models import BpeTrainerInput


def validate_input(ctx, config: BpeTrainerConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise BpeTrainerContractViolation(
            "too many candidates for bpe_trainer",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: BpeTrainerInput, config: BpeTrainerConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise BpeTrainerContractViolation("duplicate candidate ids after bpe_trainer")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise BpeTrainerContractViolation(
                "bpe_trainer introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise BpeTrainerContractViolation("bpe_trainer produced an unsorted ranking")
