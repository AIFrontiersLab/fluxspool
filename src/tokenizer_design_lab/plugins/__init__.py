"""Extension points: stage factories and lifecycle hooks."""

from tokenizer_design_lab.plugins.hooks import HookManager
from tokenizer_design_lab.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
