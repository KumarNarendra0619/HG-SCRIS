"""Convert a validated drainage raster into a directed graph."""

from __future__ import annotations

import networkx as nx
import numpy as np

from .routing import D8


def routing_graph(flow_direction: np.ndarray) -> nx.DiGraph:
    """Build a directed cell graph where edges point downstream."""
    fd = np.asarray(flow_direction)
    rows, cols = fd.shape
    graph = nx.DiGraph()
    for r in range(rows):
        for c in range(cols):
            if int(fd[r, c]) < 0:
                continue
            u = (r, c)
            graph.add_node(u)
            dr, dc, _ = D8[int(fd[r, c])]
            rr, cc = r + int(dr), c + int(dc)
            if 0 <= rr < rows and 0 <= cc < cols and int(fd[rr, cc]) >= -1:
                graph.add_edge(u, (rr, cc))
    return graph


def downstream_path(graph: nx.DiGraph, start: tuple[int, int], max_steps: int = 100000):
    """Traverse one D8 downstream path from a start cell until an outlet."""
    if start not in graph:
        raise ValueError("Start cell is not present in routing graph.")
    path = [start]
    current = start
    for _ in range(max_steps):
        successors = list(graph.successors(current))
        if not successors:
            return path
        if len(successors) != 1:
            raise ValueError("Expected at most one downstream successor per D8 cell.")
        current = successors[0]
        path.append(current)
    raise RuntimeError("Maximum routing steps exceeded; inspect DEM conditioning.")
