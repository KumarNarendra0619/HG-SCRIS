"""Graph primitives for validated glacier-to-downstream connectivity."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HydroEdge:
    upstream_id: str
    downstream_id: str
    routing_method: str
    connectivity_status: str = "pending"

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.upstream_id.strip() or not self.downstream_id.strip():
            errors.append("upstream_id and downstream_id are required")
        if self.upstream_id == self.downstream_id:
            errors.append("self-loop is not permitted")
        if not self.routing_method.strip():
            errors.append("routing_method is required")
        if self.connectivity_status not in {"not_started", "pending", "passed", "failed"}:
            errors.append("invalid connectivity_status")
        return errors


def trace_downstream(start_id: str, edges: list[HydroEdge], max_steps: int = 10000) -> list[str]:
    """Return a deterministic downstream chain; reject cycles rather than guessing."""
    if max_steps <= 0:
        raise ValueError("max_steps must be > 0")
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        if edge.validate():
            raise ValueError(f"Invalid hydro edge: {edge}")
        if edge.connectivity_status != "passed":
            continue
        adjacency.setdefault(edge.upstream_id, []).append(edge.downstream_id)

    path = [start_id]
    seen = {start_id}
    current = start_id
    for _ in range(max_steps):
        next_nodes = sorted(adjacency.get(current, []))
        if not next_nodes:
            return path
        if len(next_nodes) > 1:
            raise ValueError(f"Branching downstream network at {current}; use graph traversal, not a single chain")
        nxt = next_nodes[0]
        if nxt in seen:
            raise ValueError(f"Cycle detected at {nxt}")
        path.append(nxt)
        seen.add(nxt)
        current = nxt
    raise ValueError("max_steps exceeded")
