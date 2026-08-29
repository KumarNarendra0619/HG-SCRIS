"""Hydrographic network preparation for glacier-to-settlement routing."""

from __future__ import annotations

import geopandas as gpd


def prepare_river_network(rivers: gpd.GeoDataFrame, id_field: str) -> gpd.GeoDataFrame:
    """Validate and minimally standardize a river network.

    Direction is not inferred from line geometry. A downstream-directed network
    requires an authoritative flow-direction attribute or a DEM-derived network.
    """
    if rivers.crs is None:
        raise ValueError("River network has no CRS.")
    if id_field not in rivers.columns:
        raise ValueError(f"Missing river identifier field: {id_field}")
    out = rivers.copy()
    out = out[~out.geometry.is_empty].copy()
    out = out[out.geometry.notna()].copy()
    return out
