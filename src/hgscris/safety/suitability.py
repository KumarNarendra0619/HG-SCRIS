"""Safe-zone suitability screening."""

from __future__ import annotations


def safe_zone_screen(
    outside_hazard: bool,
    reachable: bool,
    travel_time_s: float,
    capacity: float,
    demand: float,
    elevation_gain_m: float = 0.0,
) -> dict:
    """Return transparent eligibility flags for a candidate safe zone.

    This is a screening layer; it does not certify a location as officially safe.
    """
    if travel_time_s < 0 or capacity < 0 or demand < 0:
        raise ValueError("Travel time, capacity and demand must be non-negative.")
    return {
        "outside_hazard": bool(outside_hazard),
        "reachable": bool(reachable),
        "capacity_sufficient": capacity >= demand,
        "travel_time_s": travel_time_s,
        "elevation_gain_m": elevation_gain_m,
        "eligible_screening": bool(outside_hazard and reachable and capacity >= demand),
    }
