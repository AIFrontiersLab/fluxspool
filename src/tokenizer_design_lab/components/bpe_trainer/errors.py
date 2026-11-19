"""Errors raised by BPE Trainer. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from tokenizer_design_lab.kernel.errors import StageError


class BpeTrainerError(StageError):
    code = "bpe_trainer_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("bpe_trainer", message, retryable=retryable, details=details)


class BpeTrainerContractViolation(BpeTrainerError):
    code = "bpe_trainer_contract_violation"
