"""Glacier-to-hydrography connectivity assessment."""

from __future__ import annotations

import geopandas as gpd
import pandas as pd


def connectivity_evidence(
    outlet_to_river_distance_m: float,
    routed_stream_agrees: bool,
    hydrography_agrees: bool,
) -> dict:
    """Assign evidence class without treating distance alone as flow proof."""
    if routed_stream_agrees and hydrography_agrees:
        cls = "C3"
    elif routed_stream_agrees or hydrography_agrees:
        cls = "C2"
    elif outlet_to_river_distance_m >= 0:
        cls = "C1"
    else:
        cls = "C0"
    return {
        "connectivity_class": cls,
        "outlet_to_river_distance_m": float(outlet_to_river_distance_m),
        "routed_stream_agrees": bool(routed_stream_agrees),
        "hydrography_agrees": bool(hydrography_agrees),
    }


def attach_connectivity_evidence(
    glaciers: gpd.GeoDataFrame, evidence: pd.DataFrame, id_field: str = "glacier_id"
) -> gpd.GeoDataFrame:
    """Attach precomputed connectivity evidence to glacier records."""
    if id_field not in glaciers.columns or id_field not in evidence.columns:
        raise ValueError(f"Both inputs must contain {id_field!r}.")
    return glaciers.merge(evidence, on=id_field, how="left", validate="one_to_one")
