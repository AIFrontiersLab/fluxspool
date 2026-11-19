#!/usr/bin/env bash
set -euo pipefail
export TOKENIZER_DESIGN_LAB_CONFIG=${TOKENIZER_DESIGN_LAB_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m tokenizer_design_lab serve "$@"
