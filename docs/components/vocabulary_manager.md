# Vocabulary Manager

Handles the serialization of the vocabulary and merge rules, supporting both loading and saving operations.

| Property | Value |
|---|---|
| Stage | `vocabulary_manager` |
| Role | `enrich` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/tokenizer_design_lab/components/vocabulary_manager/` |
| Tests | `tests/unit/components/test_component_vocabulary_manager.py` |

## Behaviour

Annotates candidates with structural features and collapses exact duplicates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run degrades; candidates continue without annotations.

## Metrics

- `component_vocabulary_manager_runs_total`
- `component_vocabulary_manager_candidates_out` (histogram)
- `component_vocabulary_manager_removed_total`
