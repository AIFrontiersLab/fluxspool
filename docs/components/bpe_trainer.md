# BPE Trainer

Iteratively merges the most frequent pairs of adjacent symbols in the training corpus to build the vocabulary.

| Property | Value |
|---|---|
| Stage | `bpe_trainer` |
| Role | `enrich` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/tokenizer_design_lab/components/bpe_trainer/` |
| Tests | `tests/unit/components/test_component_bpe_trainer.py` |

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

- `component_bpe_trainer_runs_total`
- `component_bpe_trainer_candidates_out` (histogram)
- `component_bpe_trainer_removed_total`
