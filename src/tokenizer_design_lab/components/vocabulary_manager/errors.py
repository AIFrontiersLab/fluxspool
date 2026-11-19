"""Errors raised by Vocabulary Manager. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from tokenizer_design_lab.kernel.errors import StageError


class VocabularyManagerError(StageError):
    code = "vocabulary_manager_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("vocabulary_manager", message, retryable=retryable, details=details)


class VocabularyManagerContractViolation(VocabularyManagerError):
    code = "vocabulary_manager_contract_violation"
