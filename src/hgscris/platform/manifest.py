"""Reproducible project manifest for the HG-SCRIS web platform."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass(frozen=True)
class ProjectManifest:
    project_id: str
    data_version: str
    model_version: str
    scenario_id: str
    crs: str
    dem_version: str
    generated_at_utc: str

    @classmethod
    def create(cls, project_id: str, data_version: str, model_version: str, scenario_id: str, crs: str, dem_version: str) -> "ProjectManifest":
        return cls(project_id, data_version, model_version, scenario_id, crs, dem_version, datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return asdict(self)
