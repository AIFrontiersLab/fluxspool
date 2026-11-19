"""Encoder/Decoder.

Converts raw text strings into integer token IDs and vice-versa, handling special tokens (e.g., , ).
"""

from tokenizer_design_lab.components.encoder_decoder.adapter import ROLE, build
from tokenizer_design_lab.components.encoder_decoder.config import CONFIG, EncoderDecoderConfig
from tokenizer_design_lab.components.encoder_decoder.errors import EncoderDecoderError
from tokenizer_design_lab.components.encoder_decoder.service import EncoderDecoderService

__all__ = ["CONFIG", "ROLE", "build", "EncoderDecoderConfig", "EncoderDecoderError", "EncoderDecoderService"]
