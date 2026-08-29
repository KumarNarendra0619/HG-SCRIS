"""Exposure linkage primitives for downstream HG-SCRIS corridors."""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot


VALID_TYPES = {
    "settlement", "population", "building", "road", "bridge", "school",
    "health", "emergency", "tourism", "critical_infrastructure",
}


@dataclass(frozen=True)
class ExposureRecord:
    exposure_id: str
    exposure_type: str
    x: float
    y: float
    source_id: str
    qa_status: str = "pending"

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.exposure_id.strip():
            errors.append("exposure_id is required")
        if self.exposure_type not in VALID_TYPES:
            errors.append("unsupported exposure_type")
        if self.qa_status not in {"not_started", "pending", "passed", "failed"}:
            errors.append("invalid qa_status")
        if not self.source_id.strip():
            errors.append("source_id is required")
        return errors


def corridor_distance(exposure: ExposureRecord, corridor_xy: list[tuple[float, float]]) -> float:
    """Euclidean screening distance in an appropriate projected CRS; not a hazard distance."""
    if exposure.validate():
        raise ValueError(exposure.validate())
    if not corridor_xy:
        raise ValueError("corridor_xy cannot be empty")
    return min(hypot(exposure.x - x, exposure.y - y) for x, y in corridor_xy)


def classify_screening_band(distance_m: float, thresholds_m: tuple[float, float]) -> str:
    """Classify proximity only; thresholds must be scenario/research-defined, never called risk."""
    near, moderate = thresholds_m
    if distance_m < 0 or near < 0 or moderate < near:
        raise ValueError("invalid thresholds or distance")
    if distance_m <= near:
        return "near_corridor"
    if distance_m <= moderate:
        return "intermediate_corridor"
    return "outside_screening_corridor"
