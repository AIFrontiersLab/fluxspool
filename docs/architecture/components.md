# Components (C4 level 3)

| # | Stage | Role | Critical | Source |
|---|---|---|---|---|
| 1 | `data_preprocessor` (Data Preprocessor) | `ingest` | yes | [component](../components/data_preprocessor.md) |
| 2 | `corpus_retrieval` (Corpus Retrieval) | `retrieve` | no | built-in |
| 3 | `bpe_trainer` (BPE Trainer) | `enrich` | no | [component](../components/bpe_trainer.md) |
| 4 | `vocabulary_manager` (Vocabulary Manager) | `enrich` | no | [component](../components/vocabulary_manager.md) |
| 5 | `ranking_cache` (Ranking Cache) | `cache` | no | [component](../components/ranking_cache.md) |
| 6 | `encoder_decoder` (Encoder/Decoder) | `score` | no | [component](../components/encoder_decoder.md) |
| 7 | `graceful_fallback` (Graceful Fallback) | `fallback` | no | built-in |
| 8 | `access_policy` (Access Policy) | `policy` | yes | built-in |
| 9 | `token_budget_governor` (Token Budget Governor) | `budget` | no | [component](../components/token_budget_governor.md) |
| 10 | `answer_assembly` (Answer Assembly) | `answer` | yes | built-in |

Each concept component follows the same internal layout so reviewers can navigate
any of them blind: `config.py`, `port.py`, `service.py`, `validators.py`, `models.py`,
`metrics.py`, `errors.py`, `adapter.py`.
