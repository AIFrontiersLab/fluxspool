"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``tokenizer_design_lab.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from tokenizer_design_lab.ports.audit import AuditSink
from tokenizer_design_lab.ports.cache import RankingCache
from tokenizer_design_lab.ports.corpus import CorpusRepository
from tokenizer_design_lab.ports.event_bus import EventBus
from tokenizer_design_lab.ports.repository import RunRepository
from tokenizer_design_lab.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
