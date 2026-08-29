"""Hazard-corridor primitives for HG-SCRIS.

A corridor is a modelled potential impact zone. It is not a probability map
unless a calibrated hazard model is supplied.
"""

from __future__ import annotations

import geopandas as gpd


def build_channel_corridor(
    channel: gpd.GeoDataFrame,
    width_m: float,
    cap_style: int = 2,
) -> gpd.GeoDataFrame:
    """Create a parameterized screening corridor around a channel.

    The input must be in a projected CRS with metre units. This is a screening
    construct, not a hydraulic inundation model.
    """
    if width_m <= 0:
        raise ValueError("Corridor width must be positive.")
    if channel.crs is None:
        raise ValueError("Channel layer has no CRS.")
    if channel.crs.is_geographic:
        raise ValueError("Project channel to a metre-based CRS before buffering.")
    out = channel.copy()
    out["corridor_width_m"] = float(width_m)
    out["hazard_model"] = "channel_buffer_screening"
    out.geometry = out.geometry.buffer(width_m, cap_style=cap_style)
    return out
