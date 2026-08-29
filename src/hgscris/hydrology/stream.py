"""Stream extraction and raster-to-vector utilities for HG-SCRIS."""

from __future__ import annotations

import numpy as np
import geopandas as gpd
from rasterio.features import shapes
from shapely.geometry import shape


def extract_stream_mask(accumulation: np.ndarray, threshold: float) -> np.ndarray:
    """Extract candidate stream cells using a documented accumulation threshold."""
    if threshold <= 0:
        raise ValueError("Stream threshold must be positive.")
    acc = np.asarray(accumulation, dtype=float)
    return np.isfinite(acc) & (acc >= threshold)


def stream_mask_polygons(mask: np.ndarray, transform, crs) -> gpd.GeoDataFrame:
    """Vectorize stream-mask cells as QA geometry; not a centerline network."""
    m = np.asarray(mask, dtype=np.uint8)
    records = []
    for geom, value in shapes(m, mask=m.astype(bool), transform=transform):
        if value == 1:
            records.append(shape(geom))
    return gpd.GeoDataFrame({"stream_candidate": [1] * len(records)}, geometry=records, crs=crs)
