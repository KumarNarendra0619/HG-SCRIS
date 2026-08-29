"""Traceable downstream network utilities."""

from __future__ import annotations

import networkx as nx


def build_network(nodes: list[dict], edges: list[dict]) -> nx.DiGraph:
    """Build a directed drainage/exposure network from validated IDs."""
    graph = nx.DiGraph()
    for node in nodes:
        if "id" not in node or "type" not in node:
            raise ValueError("Every network node requires id and type.")
        graph.add_node(node["id"], **node)
    for edge in edges:
        source, target = edge.get("source"), edge.get("target")
        if source not in graph or target not in graph:
            raise ValueError("Network edge references an unknown node.")
        graph.add_edge(source, target, **{k: v for k, v in edge.items() if k not in {"source", "target"}})
    return graph


def downstream_nodes(graph: nx.DiGraph, source_id: str, node_types: set[str] | None = None) -> list[str]:
    """Return reachable downstream nodes, optionally filtered by type."""
    if source_id not in graph:
        raise ValueError("Source node is not in network.")
    reachable = nx.descendants(graph, source_id)
    if node_types is None:
        return list(reachable)
    return [n for n in reachable if graph.nodes[n].get("type") in node_types]


def shortest_downstream_path(graph: nx.DiGraph, source_id: str, target_id: str) -> list[str]:
    """Return a directed path between source and target."""
    try:
        return nx.shortest_path(graph, source_id, target_id)
    except nx.NetworkXNoPath as exc:
        raise ValueError("No directed downstream path exists.") from exc
