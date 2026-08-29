"""Standardize glacier inventory attributes into the HG-SCRIS schema."""

from __future__ import annotations

import geopandas as gpd


def standardize_glacier_inventory(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Return a minimally standardized glacier GeoDataFrame.

    The function deliberately avoids assuming source-specific field names.
    Source mappings belong in a dataset-specific adapter/configuration layer.
    """
    out = gdf.copy()
    out.columns = [str(c).strip().lower() for c in out.columns]
    return out
