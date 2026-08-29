"""Deterministic terrain metrics used by the HG-SCRIS corridor model."""

from __future__ import annotations

import numpy as np


def slope_degrees(dem: np.ndarray, cellsize_x: float, cellsize_y: float | None = None) -> np.ndarray:
    """Calculate terrain slope in degrees from a regular DEM grid."""
    z = np.asarray(dem, dtype=float)
    if z.ndim != 2:
        raise ValueError("DEM must be a 2D array.")
    if cellsize_x <= 0 or (cellsize_y is not None and cellsize_y <= 0):
        raise ValueError("Cell sizes must be positive.")
    cy = cellsize_x if cellsize_y is None else cellsize_y
    dzdy, dzdx = np.gradient(z, cy, cellsize_x)
    return np.degrees(np.arctan(np.hypot(dzdx, dzdy)))


def local_relief(dem: np.ndarray, window: int = 3) -> np.ndarray:
    """Compute simple local relief as rolling max minus rolling min."""
    z = np.asarray(dem, dtype=float)
    if z.ndim != 2 or window < 1 or window % 2 == 0:
        raise ValueError("DEM must be 2D and window must be a positive odd integer.")
    pad = window // 2
    p = np.pad(z, pad, mode="edge")
    out = np.empty_like(z)
    for r in range(z.shape[0]):
        for c in range(z.shape[1]):
            block = p[r:r + window, c:c + window]
            out[r, c] = np.nanmax(block) - np.nanmin(block)
    return out


def longitudinal_gradient(elevation_upstream: float, elevation_downstream: float, distance_m: float) -> float:
    """Return dimensionless longitudinal channel gradient."""
    if distance_m <= 0:
        raise ValueError("Distance must be positive.")
    return (elevation_upstream - elevation_downstream) / distance_m
