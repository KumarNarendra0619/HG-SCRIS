"""Canonical glacier-record validation for HG-SCRIS."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GlacierRecord:
    source_glacier_id: str
    hgscris_glacier_id: str
    inventory_name: str
    inventory_version: str
    area_km2: float
    data_quality: str
    source_url: str
    processing_version: str
    lineage_id: str
    elevation_min_m: float | None = None
    elevation_mean_m: float | None = None
    elevation_max_m: float | None = None
    mean_slope_deg: float | None = None
    mass_balance_value: float | None = None
    ice_thickness_m: float | None = None
    volume_km3: float | None = None

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.area_km2 <= 0:
            errors.append("area_km2 must be > 0")
        if self.elevation_min_m is not None and self.elevation_max_m is not None and self.elevation_min_m > self.elevation_max_m:
            errors.append("elevation_min_m cannot exceed elevation_max_m")
        if self.mean_slope_deg is not None and not 0 <= self.mean_slope_deg <= 90:
            errors.append("mean_slope_deg must be between 0 and 90")
        if self.ice_thickness_m is not None and self.ice_thickness_m < 0:
            errors.append("ice_thickness_m cannot be negative")
        if self.volume_km3 is not None and self.volume_km3 < 0:
            errors.append("volume_km3 cannot be negative")
        if self.data_quality not in {"not_started", "pending", "passed", "failed"}:
            errors.append("invalid data_quality")
        for name, value in {
            "source_glacier_id": self.source_glacier_id,
            "hgscris_glacier_id": self.hgscris_glacier_id,
            "inventory_name": self.inventory_name,
            "inventory_version": self.inventory_version,
            "source_url": self.source_url,
            "processing_version": self.processing_version,
            "lineage_id": self.lineage_id,
        }.items():
            if not str(value).strip():
                errors.append(f"{name} is required")
        return errors
