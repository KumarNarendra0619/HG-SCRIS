"""DEM-derived terrain metrics for HG-SCRIS."""

from __future__ import annotations

import numpy as np
import rasterio
from rasterio.transform import Affine


def read_dem(path: str):
    """Read a DEM and return array plus raster metadata."""
    with rasterio.open(path) as src:
        return src.read(1, masked=True), src.profile.copy()


def slope_degrees(dem: np.ndarray, transform: Affine) -> np.ndarray:
    """Calculate first-order terrain slope in degrees using DEM spacing."""
    xres = abs(transform.a)
    yres = abs(transform.e)
    dz_dy, dz_dx = np.gradient(dem.astype(float), yres, xres)
    return np.degrees(np.arctan(np.hypot(dz_dx, dz_dy)))


def elevation_summary(values: np.ndarray) -> dict:
    """Return robust elevation summary statistics."""
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return {"count": 0}
    return {
        "count": int(arr.size),
        "min_m": float(np.min(arr)),
        "max_m": float(np.max(arr)),
        "mean_m": float(np.mean(arr)),
        "median_m": float(np.median(arr)),
    }
