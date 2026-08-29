"""Terrain and valley-morphometry validation primitives."""

from __future__ import annotations


def validate_dem_metadata(*, horizontal_crs: str, vertical_datum: str, resolution_m: float, nodata_defined: bool) -> list[str]:
    errors: list[str] = []
    if not horizontal_crs.strip():
        errors.append("horizontal_crs is required")
    if not vertical_datum.strip():
        errors.append("vertical_datum must be declared or explicitly marked unknown")
    if resolution_m <= 0:
        errors.append("resolution_m must be > 0")
    if not nodata_defined:
        errors.append("NoData definition is required")
    return errors


def validate_derived_slope(slope_min: float, slope_max: float) -> list[str]:
    errors: list[str] = []
    if slope_min < 0 or slope_max > 90 or slope_min > slope_max:
        errors.append("slope range must satisfy 0 <= min <= max <= 90")
    return errors


def valley_confinement_index(valley_width_m: float, channel_width_m: float) -> float:
    """Simple geometric screening ratio; not a hydraulic hazard metric."""
    if valley_width_m <= 0 or channel_width_m < 0:
        raise ValueError("Widths must be positive/non-negative.")
    return channel_width_m / valley_width_m
