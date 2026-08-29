"""Deterministic terrain metric helpers for HG-SCRIS.

These helpers operate on already QA'd numerical arrays. They do not select a
DEM, infer vertical datum, or claim hydrodynamic hazard from terrain alone.
"""

from __future__ import annotations

import math


def slope_degrees(dzdx: float, dzdy: float) -> float:
    """Calculate local slope angle in degrees from elevation gradients."""
    return math.degrees(math.atan(math.sqrt(dzdx * dzdx + dzdy * dzdy)))


def relief(elevation_min_m: float, elevation_max_m: float) -> float:
    """Calculate relief; negative relief indicates invalid input."""
    value = elevation_max_m - elevation_min_m
    if value < 0:
        raise ValueError("elevation_max_m must be >= elevation_min_m")
    return value


def validate_terrain_record(*, cell_size_m: float, elevation_min_m: float, elevation_max_m: float) -> list[str]:
    errors: list[str] = []
    if cell_size_m <= 0:
        errors.append("cell_size_m must be > 0")
    if elevation_max_m < elevation_min_m:
        errors.append("elevation range is invalid")
    return errors
