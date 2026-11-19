"""BPE Trainer.

Iteratively merges the most frequent pairs of adjacent symbols in the training corpus to build the vocabulary.
"""

from tokenizer_design_lab.components.bpe_trainer.adapter import ROLE, build
from tokenizer_design_lab.components.bpe_trainer.config import CONFIG, BpeTrainerConfig
from tokenizer_design_lab.components.bpe_trainer.errors import BpeTrainerError
from tokenizer_design_lab.components.bpe_trainer.service import BpeTrainerService

__all__ = ["CONFIG", "ROLE", "build", "BpeTrainerConfig", "BpeTrainerError", "BpeTrainerService"]
