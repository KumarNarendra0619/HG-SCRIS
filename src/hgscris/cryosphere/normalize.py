"""Normalization rules for HG-SCRIS glacier and glacial-lake records."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GlacierRecord:
    glacier_id: str
    source_id: str
    geometry_ref: str
    source_date: str
    area_km2: float | None = None
    min_elev_m: float | None = None
    max_elev_m: float | None = None

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.glacier_id.strip():
            errors.append("glacier_id is required")
        if not self.source_id.strip():
            errors.append("source_id is required")
        if not self.geometry_ref.strip():
            errors.append("geometry_ref is required")
        if not self.source_date.strip():
            errors.append("source_date is required")
        if self.area_km2 is not None and self.area_km2 <= 0:
            errors.append("area_km2 must be > 0")
        if self.min_elev_m is not None and self.max_elev_m is not None and self.min_elev_m > self.max_elev_m:
            errors.append("min_elev_m cannot exceed max_elev_m")
        return errors


def normalize_id(source: str, raw_id: str) -> str:
    """Create a stable HG-SCRIS source-qualified key; never overwrite the source ID."""
    source = source.strip().upper().replace(" ", "_")
    raw_id = raw_id.strip()
    if not source or not raw_id:
        raise ValueError("source and raw_id are required")
    return f"{source}:{raw_id}"


def detect_duplicate_ids(ids: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in ids:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return sorted(duplicates)
