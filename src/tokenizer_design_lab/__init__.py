"""Tokenizer Design Lab: governed reference service.

Tokenizer Design Lab: Engineering Tokenization for Domain-Specific LLMs

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from tokenizer_design_lab.application.pipeline import run
from tokenizer_design_lab.container import build_container
from tokenizer_design_lab.version import __version__

__all__ = ["__version__", "build_container", "run"]
