"""Concept-specific components. Each one specialises a stage role with its own
configuration, validation, metrics, and errors."""

from tokenizer_design_lab.components.bpe_trainer import adapter as _bpe_trainer
from tokenizer_design_lab.components.data_preprocessor import adapter as _data_preprocessor
from tokenizer_design_lab.components.encoder_decoder import adapter as _encoder_decoder
from tokenizer_design_lab.components.ranking_cache import adapter as _ranking_cache
from tokenizer_design_lab.components.token_budget_governor import adapter as _token_budget_governor
from tokenizer_design_lab.components.vocabulary_manager import adapter as _vocabulary_manager

COMPONENT_FACTORIES = {
    "data_preprocessor": (_data_preprocessor.ROLE, _data_preprocessor.build),
    "bpe_trainer": (_bpe_trainer.ROLE, _bpe_trainer.build),
    "vocabulary_manager": (_vocabulary_manager.ROLE, _vocabulary_manager.build),
    "encoder_decoder": (_encoder_decoder.ROLE, _encoder_decoder.build),
    "ranking_cache": (_ranking_cache.ROLE, _ranking_cache.build),
    "token_budget_governor": (_token_budget_governor.ROLE, _token_budget_governor.build),
}
