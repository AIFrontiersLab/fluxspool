"""Errors raised by Data Preprocessor. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from tokenizer_design_lab.kernel.errors import StageError


class DataPreprocessorError(StageError):
    code = "data_preprocessor_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("data_preprocessor", message, retryable=retryable, details=details)


class DataPreprocessorContractViolation(DataPreprocessorError):
    code = "data_preprocessor_contract_violation"
