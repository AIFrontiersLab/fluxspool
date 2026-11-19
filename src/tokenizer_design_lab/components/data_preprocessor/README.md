# Data Preprocessor

Cleans and normalizes domain-specific text to ensure consistent character encoding.

| Property | Value |
|---|---|
| Stage name | `data_preprocessor` |
| Role | `ingest` |
| Interface | `process(ctx) -> None` |
| Critical | Yes. A failure stops the run. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `DataPreprocessorService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Validates, normalises, de-duplicates, and bounds the incoming candidate set.

See also [`docs/components/data_preprocessor.md`](../../../../docs/components/data_preprocessor.md).
