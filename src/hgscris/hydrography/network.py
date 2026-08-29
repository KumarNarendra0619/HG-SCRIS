"""Hydrography connectivity primitives for HG-SCRIS."""

from __future__ import annotations


def validate_reach(*, reach_id: str, length_m: float, upstream_id: str | None, downstream_id: str | None) -> list[str]:
    errors: list[str] = []
    if not reach_id:
        errors.append("reach_id is required")
    if length_m <= 0:
        errors.append("length_m must be > 0")
    if upstream_id == reach_id or downstream_id == reach_id:
        errors.append("a reach cannot point to itself")
    return errors


def downstream_chain(graph: dict[str, str | None], start_id: str, max_steps: int = 10000) -> list[str]:
    """Return a downstream reach chain and flag loops through ValueError."""
    chain: list[str] = []
    seen: set[str] = set()
    current: str | None = start_id
    while current is not None:
        if current in seen:
            raise ValueError(f"cycle detected at reach {current}")
        if len(chain) >= max_steps:
            raise ValueError("maximum downstream traversal exceeded")
        seen.add(current)
        chain.append(current)
        current = graph.get(current)
    return chain
