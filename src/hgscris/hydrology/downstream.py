"""Downstream connectivity primitives for HG-SCRIS."""

from __future__ import annotations

import geopandas as gpd
from shapely.geometry import Point


def nearest_river_seed(point: Point, rivers: gpd.GeoDataFrame) -> tuple[int, float]:
    """Find the nearest river feature and distance in the layer CRS.

    This is a spatial seed only. It does not prove downstream connectivity.
    Production routing must use flow direction/topology in BUILD-01G+.
    """
    if rivers.empty:
        raise ValueError("River network is empty.")
    distances = rivers.geometry.distance(point)
    idx = distances.idxmin()
    return idx, float(distances.loc[idx])
