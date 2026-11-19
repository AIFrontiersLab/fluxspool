"""Pre- and post-conditions for Vocabulary Manager.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from tokenizer_design_lab.components.vocabulary_manager.config import VocabularyManagerConfig
from tokenizer_design_lab.components.vocabulary_manager.errors import VocabularyManagerContractViolation
from tokenizer_design_lab.components.vocabulary_manager.models import VocabularyManagerInput


def validate_input(ctx, config: VocabularyManagerConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise VocabularyManagerContractViolation(
            "too many candidates for vocabulary_manager",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: VocabularyManagerInput, config: VocabularyManagerConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise VocabularyManagerContractViolation("duplicate candidate ids after vocabulary_manager")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise VocabularyManagerContractViolation(
                "vocabulary_manager introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise VocabularyManagerContractViolation("vocabulary_manager produced an unsorted ranking")
