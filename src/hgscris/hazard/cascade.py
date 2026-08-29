"""Rule-based multi-hazard cascade graph for HG-SCRIS.

This layer represents causal/physical links between hazard-process nodes. It is
not a calibrated probability model. Edges carry evidence and status so that
unsupported links cannot silently become quantitative risk.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
import networkx as nx


ALLOWED_NODE_TYPES = {
    "glacier", "lake", "trigger", "ice", "rock", "water", "debris",
    "sediment", "stream", "tributary", "river", "water_body",
    "settlement", "infrastructure", "impact"
}


@dataclass(frozen=True)
class CascadeEdge:
    source: str
    target: str
    process: str
    evidence_class: str = "C0"
    status: str = "candidate"

    def to_dict(self) -> dict:
        return asdict(self)


def build_cascade_graph(nodes: list[dict], edges: list[CascadeEdge]) -> nx.DiGraph:
    """Build and validate a directed cascade graph."""
    graph = nx.DiGraph()
    for node in nodes:
        if node.get("type") not in ALLOWED_NODE_TYPES:
            raise ValueError(f"Unsupported cascade node type: {node.get('type')}")
        graph.add_node(node["id"], **node)
    for edge in edges:
        if edge.source not in graph or edge.target not in graph:
            raise ValueError("Cascade edge references an unknown node.")
        if edge.evidence_class not in {"C3", "C2", "C1", "C0"}:
            raise ValueError("Invalid evidence class.")
        graph.add_edge(edge.source, edge.target, **edge.to_dict())
    return graph


def downstream_processes(graph: nx.DiGraph, start_id: str) -> list[str]:
    """Return reachable downstream process nodes in graph order."""
    if start_id not in graph:
        raise ValueError("Start node is not in cascade graph.")
    return list(nx.descendants(graph, start_id))
