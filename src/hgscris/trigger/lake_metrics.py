"""Glacial-lake source metrics and quality controls."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class LakeMetrics:
    """Versioned lake observations used as trigger-screening inputs."""

    lake_id: str
    area_m2: float
    elevation_m: float | None = None
    volume_m3: float | None = None
    observation_date: str | None = None
    source: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def validate_lake_metrics(metrics: LakeMetrics) -> LakeMetrics:
    """Validate physically plausible source metrics without inferring hazard."""
    if not metrics.lake_id:
        raise ValueError("lake_id is required.")
    if metrics.area_m2 <= 0:
        raise ValueError("Lake area must be positive.")
    if metrics.elevation_m is not None and metrics.elevation_m < -100:
        raise ValueError("Lake elevation is outside the expected terrestrial range.")
    if metrics.volume_m3 is not None and metrics.volume_m3 <= 0:
        raise ValueError("Lake volume must be positive when supplied.")
    return metrics
