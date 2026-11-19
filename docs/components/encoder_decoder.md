# Encoder/Decoder

Converts raw text strings into integer token IDs and vice-versa, handling special tokens (e.g., , ).

| Property | Value |
|---|---|
| Stage | `encoder_decoder` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/tokenizer_design_lab/components/encoder_decoder/` |
| Tests | `tests/unit/components/test_component_encoder_decoder.py` |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Output is sorted by descending score.

## On failure

Run degrades; fallback restores upstream prior order.

## Metrics

- `component_encoder_decoder_runs_total`
- `component_encoder_decoder_candidates_out` (histogram)
- `component_encoder_decoder_removed_total`
