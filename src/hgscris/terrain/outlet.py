"""Glacier outlet preparation for downstream routing.

This module does not claim a hydrologically correct outlet from a glacier
polygon alone. It provides a reproducible candidate outlet definition that can
later be snapped to a validated drainage network.
"""

from __future__ import annotations

import geopandas as gpd
from shapely.geometry import Point


def candidate_outlet_from_lowest_vertex(glacier: gpd.GeoSeries) -> Point:
    """Return a candidate outlet as the lowest-geometry vertex.

    Elevation is not available in a plain GeoSeries, so this function is a
    geometry-only placeholder and should not be used for production routing.
    Use DEM-conditioned outlet extraction in the next hydrology build.
    """
    coords = []
    for geom in glacier.geometry if hasattr(glacier, "geometry") else glacier:
        if geom is None or geom.is_empty:
            continue
        coords.extend(list(geom.exterior.coords) if hasattr(geom, "exterior") else [])
    if not coords:
        raise ValueError("No polygon vertices available for candidate outlet.")
    x, y = coords[0]
    return Point(x, y)
