"""Comparable geometry-change calculations."""

from __future__ import annotations


def area_change(start_area_m2: float, end_area_m2: float) -> dict:
    """Return absolute and relative polygon-area change."""
    if start_area_m2 <= 0 or end_area_m2 < 0:
        raise ValueError("Areas must be non-negative and baseline area must be positive.")
    delta = end_area_m2 - start_area_m2
    return {
        "absolute_change_m2": delta,
        "relative_change": delta / start_area_m2,
    }
