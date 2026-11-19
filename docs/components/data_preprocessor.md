# Data Preprocessor

Cleans and normalizes domain-specific text to ensure consistent character encoding.

| Property | Value |
|---|---|
| Stage | `data_preprocessor` |
| Role | `ingest` |
| Interface | `process(ctx) -> None` |
| Critical | yes |
| Source | `src/tokenizer_design_lab/components/data_preprocessor/` |
| Tests | `tests/unit/components/test_component_data_preprocessor.py` |

## Behaviour

Validates, normalises, de-duplicates, and bounds the incoming candidate set.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- May introduce new candidate ids.
- Ordering is preserved or intentionally changed per role.

## On failure

Run fails; the request never reaches retrieval.

## Metrics

- `component_data_preprocessor_runs_total`
- `component_data_preprocessor_candidates_out` (histogram)
- `component_data_preprocessor_removed_total`
