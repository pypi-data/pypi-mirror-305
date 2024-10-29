"""
This type stub file was generated by pyright.
"""

from typing import Optional
from collections.abc import Iterable

def subdict(d, keys): # -> dict[Any, Any]:
    ...

_reranker = ...
def upsert_reranker_model(model_name=..., device=..., **kwargs): # -> CrossEncoder:
    ...

_ALL_RERANK_ELEMENTS = ...
_INCLUDE_MAP = ...
def rerank(universe: Iterable[str], query: str, cross_encoder=..., include: Optional[Iterable[str]] = ..., *args, **kwargs): # -> list[tuple[str, ...]]:
    ...

