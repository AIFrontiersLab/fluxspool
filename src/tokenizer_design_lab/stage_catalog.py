"""Stage catalog for Tokenizer Design Lab.

Declares the default stage order and registers every built-in and component stage
with the plugin registry. Imports of stage classes are deferred so configuration
modules can read ``DEFAULT_STAGE_ORDER`` without import cycles.
"""

from __future__ import annotations

DEFAULT_STAGE_ORDER = [
    "data_preprocessor",
    "corpus_retrieval",
    "bpe_trainer",
    "vocabulary_manager",
    "ranking_cache",
    "encoder_decoder",
    "graceful_fallback",
    "access_policy",
    "token_budget_governor",
    "answer_assembly",
]

BUILTINS = {
    "intake": "ingest",
    "corpus_retrieval": "retrieve",
    "relevance_scoring": "score",
    "access_policy": "policy",
    "graceful_fallback": "fallback",
    "answer_assembly": "answer",
}

COMPONENTS = [
    {"name": 'Data Preprocessor', "slug": "data_preprocessor", "role": "ingest", "origin": "spec"},
    {"name": 'BPE Trainer', "slug": "bpe_trainer", "role": "enrich", "origin": "spec"},
    {"name": 'Vocabulary Manager', "slug": "vocabulary_manager", "role": "enrich", "origin": "spec"},
    {"name": 'Encoder/Decoder', "slug": "encoder_decoder", "role": "score", "origin": "spec"},
    {"name": 'Ranking Cache', "slug": "ranking_cache", "role": "cache", "origin": "padded"},
    {"name": 'Token Budget Governor', "slug": "token_budget_governor", "role": "budget", "origin": "padded"},
]


def register_all(registry) -> None:
    from tokenizer_design_lab.components import COMPONENT_FACTORIES
    from tokenizer_design_lab.stages import ROLE_CLASSES

    for name, role in BUILTINS.items():
        cls = ROLE_CLASSES[role]
        registry.register(name, role, lambda services, cls=cls, name=name: cls(name, services), source="builtin")
    for name, (role, factory) in COMPONENT_FACTORIES.items():
        registry.register(name, role, factory, source="component")
