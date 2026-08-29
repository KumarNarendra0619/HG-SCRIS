"""Geometry QC and measurement utilities for extracted glacier/lake polygons."""

from __future__ import annotations

import geopandas as gpd


def validate_polygons(layer: gpd.GeoDataFrame, id_field: str) -> gpd.GeoDataFrame:
    """Validate identifiers and return non-empty polygon geometries."""
    if layer.crs is None:
        raise ValueError("Extraction layer has no CRS.")
    if id_field not in layer.columns:
        raise ValueError(f"Missing identifier field: {id_field}")
    if layer.geometry.geom_type.isin(["Polygon", "MultiPolygon"]).all() is False:
        raise ValueError("Extraction layer must contain polygon or multipolygon geometries only.")
    out = layer.copy()
    out = out[out.geometry.notna() & ~out.geometry.is_empty].copy()
    if out[id_field].duplicated().any():
        raise ValueError(f"Duplicate {id_field} values detected.")
    return out


def add_area(layer: gpd.GeoDataFrame, area_field: str = "area_m2") -> gpd.GeoDataFrame:
    """Add planar area; input must use a projected CRS with metre units."""
    if layer.crs is None or layer.crs.is_geographic:
        raise ValueError("Project polygons to a metre-based CRS before area calculation.")
    out = layer.copy()
    out[area_field] = out.geometry.area
    return out
