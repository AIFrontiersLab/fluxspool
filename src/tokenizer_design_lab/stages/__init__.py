"""Role implementations. Components specialise one of these strategies."""

from tokenizer_design_lab.stages.answer import AnswerStage
from tokenizer_design_lab.stages.approval import ApprovalStage
from tokenizer_design_lab.stages.audit import AuditStage
from tokenizer_design_lab.stages.base import Stage, StageServices
from tokenizer_design_lab.stages.budget import BudgetStage
from tokenizer_design_lab.stages.cache import CacheStage
from tokenizer_design_lab.stages.enrich import EnrichStage
from tokenizer_design_lab.stages.fallback import FallbackStage
from tokenizer_design_lab.stages.ingest import IngestStage
from tokenizer_design_lab.stages.policy import PolicyStage
from tokenizer_design_lab.stages.retrieve import RetrieveStage
from tokenizer_design_lab.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
