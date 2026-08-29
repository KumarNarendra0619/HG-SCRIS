"""Spatial exposure primitives for downstream hazard corridors."""

from __future__ import annotations

import geopandas as gpd


def prepare_settlements(settlements: gpd.GeoDataFrame, id_field: str = "settlement_id") -> gpd.GeoDataFrame:
    """Validate settlement inventory without altering source geometries."""
    if settlements.crs is None:
        raise ValueError("Settlement layer has no CRS.")
    if id_field not in settlements.columns:
        raise ValueError(f"Missing settlement identifier field: {id_field}")
    out = settlements.copy()
    return out[out.geometry.notna() & ~out.geometry.is_empty].copy()


def intersect_corridor(
    settlements: gpd.GeoDataFrame,
    corridor: gpd.GeoDataFrame,
    settlement_id: str = "settlement_id",
) -> gpd.GeoDataFrame:
    """Return settlements spatially intersecting a candidate hazard corridor.

    This is exposure screening only; intersection does not imply damage or
    hazard probability.
    """
    if settlements.crs != corridor.crs:
        corridor = corridor.to_crs(settlements.crs)
    if settlement_id not in settlements.columns:
        raise ValueError(f"Missing settlement identifier field: {settlement_id}")
    return gpd.sjoin(settlements, corridor[["geometry"]], predicate="intersects", how="inner")
