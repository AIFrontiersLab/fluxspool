"""Pre- and post-conditions for Encoder/Decoder.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from tokenizer_design_lab.components.encoder_decoder.config import EncoderDecoderConfig
from tokenizer_design_lab.components.encoder_decoder.errors import EncoderDecoderContractViolation
from tokenizer_design_lab.components.encoder_decoder.models import EncoderDecoderInput


def validate_input(ctx, config: EncoderDecoderConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise EncoderDecoderContractViolation(
            "too many candidates for encoder_decoder",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: EncoderDecoderInput, config: EncoderDecoderConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise EncoderDecoderContractViolation("duplicate candidate ids after encoder_decoder")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise EncoderDecoderContractViolation(
                "encoder_decoder introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise EncoderDecoderContractViolation("encoder_decoder produced an unsorted ranking")
