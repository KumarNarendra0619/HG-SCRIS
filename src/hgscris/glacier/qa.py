"""Quality assurance checks for standardized glacier inventories."""

from __future__ import annotations

import geopandas as gpd
import pandas as pd


def glacier_qa_report(gdf: gpd.GeoDataFrame) -> dict:
    """Return machine-readable QA metrics without modifying the input."""
    area = pd.to_numeric(gdf.get("area_km2"), errors="coerce")
    zmin = pd.to_numeric(gdf.get("elevation_min_m"), errors="coerce")
    zmax = pd.to_numeric(gdf.get("elevation_max_m"), errors="coerce")
    zmean = pd.to_numeric(gdf.get("elevation_mean_m"), errors="coerce")

    return {
        "records": int(len(gdf)),
        "missing_rgi_id": int(gdf["rgi_id"].isna().sum()),
        "duplicate_rgi_id": int(gdf["rgi_id"].duplicated(keep=False).sum()),
        "missing_geometry": int(gdf.geometry.is_empty.sum()),
        "invalid_geometry": int((~gdf.geometry.is_valid).sum()),
        "missing_area": int(area.isna().sum()),
        "nonpositive_area": int((area <= 0).fillna(False).sum()),
        "invalid_elevation_order": int((zmax < zmin).fillna(False).sum()),
        "mean_outside_range": int(((zmean < zmin) | (zmean > zmax)).fillna(False).sum()),
    }
