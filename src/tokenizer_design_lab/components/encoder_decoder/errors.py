"""Errors raised by Encoder/Decoder. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from tokenizer_design_lab.kernel.errors import StageError


class EncoderDecoderError(StageError):
    code = "encoder_decoder_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("encoder_decoder", message, retryable=retryable, details=details)


class EncoderDecoderContractViolation(EncoderDecoderError):
    code = "encoder_decoder_contract_violation"
