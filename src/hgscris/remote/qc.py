"""Input quality-control helpers for raster-derived HG-SCRIS products."""

from __future__ import annotations

import numpy as np


def validate_raster_array(array: np.ndarray, expected_ndim: int = 2) -> dict:
    """Return basic QC diagnostics without modifying source data."""
    a = np.asarray(array)
    if a.ndim != expected_ndim:
        raise ValueError(f"Expected {expected_ndim}D raster, got {a.ndim}D.")
    finite = np.isfinite(a)
    return {
        "rows": int(a.shape[0]),
        "cols": int(a.shape[1]),
        "finite_fraction": float(finite.mean()) if a.size else 0.0,
        "min": float(np.nanmin(a)) if finite.any() else None,
        "max": float(np.nanmax(a)) if finite.any() else None,
    }
