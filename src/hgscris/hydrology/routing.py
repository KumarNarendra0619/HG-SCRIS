"""DEM-based D8 flow-routing primitives for HG-SCRIS.

This module operates on a hydrologically conditioned DEM. Conditioning itself
must be documented separately because fill/breach choices can materially change
connectivity in glacier valleys.
"""

from __future__ import annotations

import numpy as np

# D8 neighbours: row, col, distance multiplier
D8 = np.array([
    (-1, -1, np.sqrt(2)), (-1, 0, 1.0), (-1, 1, np.sqrt(2)),
    (0, -1, 1.0),                         (0, 1, 1.0),
    (1, -1, np.sqrt(2)),  (1, 0, 1.0),  (1, 1, np.sqrt(2)),
], dtype=float)


def d8_flow_direction(dem: np.ndarray) -> np.ndarray:
    """Return downstream neighbour index (0..7) for each DEM cell.

    A cell routes to the neighbour with the steepest positive downhill drop.
    ``-1`` denotes nodata, an edge without a valid neighbour, or a local sink.
    Flat/sink resolution is intentionally not hidden in this primitive.
    """
    z = np.asarray(dem, dtype=float)
    if z.ndim != 2:
        raise ValueError("DEM must be a 2-D array.")
    rows, cols = z.shape
    direction = np.full((rows, cols), -1, dtype=np.int8)

    for r in range(rows):
        for c in range(cols):
            if not np.isfinite(z[r, c]):
                continue
            best_slope = 0.0
            best_idx = -1
            for i, (dr, dc, dist) in enumerate(D8):
                rr, cc = r + int(dr), c + int(dc)
                if 0 <= rr < rows and 0 <= cc < cols and np.isfinite(z[rr, cc]):
                    s = (z[r, c] - z[rr, cc]) / dist
                    if s > best_slope:
                        best_slope, best_idx = s, i
            direction[r, c] = best_idx
    return direction


def flow_accumulation(flow_direction: np.ndarray) -> np.ndarray:
    """Calculate unit-cell D8 flow accumulation.

    Cells with no downstream neighbour are treated as outlets. A cycle raises
    an error rather than silently producing a misleading accumulation surface.
    """
    fd = np.asarray(flow_direction)
    rows, cols = fd.shape
    acc = np.ones((rows, cols), dtype=float)
    state = np.zeros((rows, cols), dtype=np.int8)  # 0 unseen, 1 active, 2 done

    def downstream(r: int, c: int):
        i = int(fd[r, c])
        if i < 0:
            return None
        dr, dc, _ = D8[i]
        rr, cc = r + int(dr), c + int(dc)
        if not (0 <= rr < rows and 0 <= cc < cols):
            return None
        return rr, cc

    def visit(r: int, c: int) -> float:
        if not np.isfinite(fd[r, c]):
            return 0.0
        if state[r, c] == 2:
            return acc[r, c]
        if state[r, c] == 1:
            raise ValueError("Flow-direction cycle detected.")
        state[r, c] = 1
        nxt = downstream(r, c)
        if nxt is not None:
            nr, nc = nxt
            acc[nr, nc] += visit(r, c) if False else 0.0
        state[r, c] = 2
        return acc[r, c]

    # Aggregate upstream contributions by topological propagation.
    indegree = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            nxt = downstream(r, c)
            if nxt is not None:
                indegree[nxt] += 1

    queue = [(r, c) for r in range(rows) for c in range(cols) if np.isfinite(fd[r, c]) and indegree[r, c] == 0]
    processed = 0
    while queue:
        r, c = queue.pop()
        processed += 1
        nxt = downstream(r, c)
        if nxt is not None:
            nr, nc = nxt
            acc[nr, nc] += acc[r, c]
            indegree[nr, nc] -= 1
            if indegree[nr, nc] == 0:
                queue.append((nr, nc))

    valid = np.isfinite(fd)
    if processed != int(valid.sum()):
        raise ValueError("Flow-direction graph contains a cycle or unresolved dependency.")
    return acc
