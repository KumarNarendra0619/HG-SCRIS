"""RGI 7.x adapter for HG-SCRIS.

The adapter is deliberately tolerant of source field aliases because RGI products
may be distributed in different formats. Exact source fields are recorded rather
than silently inventing missing values.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import geopandas as gpd
import pandas as pd

ALIASES = {
    "rgi_id": ["rgi_id", "rgiid", "rgi_id6", "rgiid6"],
    "glacier_name": ["glac_name", "glacier_name", "name"],
    "area_km2": ["area_km2", "area", "area_km2_"],
    "elevation_min_m": ["zmin_m", "zmin", "min_elev", "elev_min"],
    "elevation_max_m": ["zmax_m", "zmax", "max_elev", "elev_max"],
    "elevation_mean_m": ["zmed_m", "zmed", "mean_elev", "elev_mean"],
}


def _first_existing(columns: Iterable[str], candidates: Iterable[str]) -> str | None:
    lookup = {str(c).lower(): c for c in columns}
    for candidate in candidates:
        if candidate.lower() in lookup:
            return lookup[candidate.lower()]
    return None


def standardize_rgi(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Map recognized RGI attributes to HG-SCRIS canonical names.

    Missing source attributes are retained as NA; they are never estimated here.
    """
    out = gdf.copy()
    out.columns = [str(c).strip().lower() for c in out.columns]
    result = gpd.GeoDataFrame(index=out.index, geometry=out.geometry, crs=out.crs)

    for target, candidates in ALIASES.items():
        source = _first_existing(out.columns, candidates)
        result[target] = out[source] if source else pd.NA

    result["glacier_id"] = result["rgi_id"].astype("string")
    result["area_km2"] = pd.to_numeric(result["area_km2"], errors="coerce")
    for field in ["elevation_min_m", "elevation_max_m", "elevation_mean_m"]:
        result[field] = pd.to_numeric(result[field], errors="coerce")

    return result


def ingest_rgi(path: str | Path) -> gpd.GeoDataFrame:
    """Read an RGI vector source and return the canonical HG-SCRIS schema."""
    gdf = gpd.read_file(path)
    if gdf.crs is None:
        raise ValueError("RGI source has no CRS; ingestion stopped.")
    if gdf.geometry.is_empty.any() or (~gdf.geometry.is_valid).any():
        raise ValueError("RGI source contains empty or invalid geometries; ingestion stopped.")
    return standardize_rgi(gdf)
