# Vocabulary Manager

Handles the serialization of the vocabulary and merge rules, supporting both loading and saving operations.

| Property | Value |
|---|---|
| Stage name | `vocabulary_manager` |
| Role | `enrich` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `VocabularyManagerService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Annotates candidates with structural features and collapses exact duplicates.

See also [`docs/components/vocabulary_manager.md`](../../../../docs/components/vocabulary_manager.md).
