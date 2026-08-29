"""Exposure metrics for settlements and infrastructure."""

from __future__ import annotations

import geopandas as gpd
import pandas as pd


def summarize_exposure(
    exposed: gpd.GeoDataFrame,
    population_field: str | None = None,
    infrastructure_fields: list[str] | None = None,
) -> dict:
    """Summarize screened exposure; missing attributes remain unknown."""
    infrastructure_fields = infrastructure_fields or []
    result = {"settlements_exposed": int(len(exposed))}
    if population_field and population_field in exposed.columns:
        result["population_exposed"] = float(pd.to_numeric(exposed[population_field], errors="coerce").sum(min_count=1))
    else:
        result["population_exposed"] = None
    result["infrastructure_counts"] = {
        field: int(pd.to_numeric(exposed[field], errors="coerce").fillna(0).sum())
        for field in infrastructure_fields
        if field in exposed.columns
    }
    return result
