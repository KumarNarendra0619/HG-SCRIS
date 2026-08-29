"""Transparent, constraint-aware evacuation-network primitives."""

from __future__ import annotations

import networkx as nx


def shortest_safe_route(
    graph: nx.Graph,
    origin: str,
    safe_nodes: set[str],
    blocked: set[str] | None = None,
    max_travel_time_s: float | None = None,
) -> list[str]:
    """Find the shortest reachable route to a safe node under declared constraints."""
    if origin not in graph:
        raise ValueError("Origin is not in the evacuation network.")
    blocked = blocked or set()
    allowed = [n for n in graph.nodes if n not in blocked or n == origin]
    subgraph = graph.subgraph(allowed)
    candidates = []
    for target in safe_nodes:
        if target in subgraph and nx.has_path(subgraph, origin, target):
            path = nx.shortest_path(subgraph, origin, target, weight="travel_time_s")
            travel_time = route_travel_time(subgraph, path)
            if max_travel_time_s is None or travel_time <= max_travel_time_s:
                candidates.append((travel_time, target, path))
    if not candidates:
        raise ValueError("No reachable safe location exists under the current constraints.")
    _, _, path = min(candidates, key=lambda x: (x[0], x[1]))
    return path


def route_travel_time(graph: nx.Graph, path: list[str]) -> float:
    """Sum non-negative travel_time_s along a route."""
    if len(path) < 2:
        return 0.0
    total = 0.0
    for a, b in zip(path, path[1:]):
        if not graph.has_edge(a, b):
            raise ValueError("Path contains a non-existent edge.")
        value = graph.edges[a, b].get("travel_time_s")
        if value is None or value < 0:
            raise ValueError("Each route edge requires non-negative travel_time_s.")
        total += float(value)
    return total


def route_safety_margin(
    graph: nx.Graph,
    path: list[str],
    hazard_arrival_time_s: float | None,
    response_delay_s: float = 0.0,
) -> float | None:
    """Return hazard-arrival minus response/travel time; None if no arrival time is supplied."""
    if hazard_arrival_time_s is None:
        return None
    if response_delay_s < 0:
        raise ValueError("response_delay_s must be non-negative")
    return float(hazard_arrival_time_s) - response_delay_s - route_travel_time(graph, path)


def route_is_time_safe(
    graph: nx.Graph,
    path: list[str],
    hazard_arrival_time_s: float | None,
    response_delay_s: float = 0.0,
) -> bool | None:
    """Evaluate temporal safety only when a hazard-arrival time is explicitly available."""
    margin = route_safety_margin(graph, path, hazard_arrival_time_s, response_delay_s)
    return None if margin is None else margin >= 0.0
