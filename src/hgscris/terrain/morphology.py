"""Terrain and valley morphology metrics for HG-SCRIS."""

from __future__ import annotations

import numpy as np


def slope_degrees(dzdx: np.ndarray, dzdy: np.ndarray) -> np.ndarray:
    """Calculate terrain slope in degrees from elevation gradients."""
    return np.degrees(np.arctan(np.hypot(dzdx, dzdy)))


def longitudinal_gradient(elevation_upstream_m: float, elevation_downstream_m: float, distance_m: float) -> float:
    """Return signed channel/valley gradient as elevation drop per metre."""
    if distance_m <= 0:
        raise ValueError("distance_m must be positive.")
    return (elevation_upstream_m - elevation_downstream_m) / distance_m


def normalized_relief(elevation: np.ndarray) -> float:
    """Return normalized relief range for a non-empty elevation array."""
    z = np.asarray(elevation, dtype=float)
    finite = z[np.isfinite(z)]
    if finite.size == 0:
        raise ValueError("Elevation array contains no finite values.")
    span = float(finite.max() - finite.min())
    return span
