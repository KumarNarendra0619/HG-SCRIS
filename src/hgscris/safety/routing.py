"""Transparent evacuation-network primitives."""

from __future__ import annotations

import networkx as nx


def shortest_safe_route(graph: nx.Graph, origin: str, safe_nodes: set[str], blocked: set[str] | None = None) -> list[str]:
    """Find the shortest route to a reachable safe node, avoiding blocked nodes."""
    if origin not in graph:
        raise ValueError("Origin is not in the evacuation network.")
    blocked = blocked or set()
    allowed = [n for n in graph.nodes if n not in blocked or n == origin]
    subgraph = graph.subgraph(allowed)
    candidates = []
    for target in safe_nodes:
        if target in subgraph and nx.has_path(subgraph, origin, target):
            candidates.append((nx.shortest_path_length(subgraph, origin, target, weight="travel_time_s"), target))
    if not candidates:
        raise ValueError("No reachable safe location exists under the current constraints.")
    _, target = min(candidates)
    return nx.shortest_path(subgraph, origin, target, weight="travel_time_s")


def route_travel_time(graph: nx.Graph, path: list[str]) -> float:
    """Sum travel_time_s along a route."""
    if len(path) < 2:
        return 0.0
    total = 0.0
    for a, b in zip(path, path[1:]):
        if not graph.has_edge(a, b):
            raise ValueError("Path contains a non-existent edge.")
        value = graph.edges[a, b].get("travel_time_s")
        if value is None or value < 0:
            raise ValueError("Each route edge requires non-negative travel_time_s.")
        total += value
    return total
