"""Scenario definitions for multi-hazard cascade modelling."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class CascadeScenario:
    """A reproducible hazard scenario descriptor."""

    scenario_id: str
    trigger_type: str
    forcing_class: str
    corridor_method: str
    parameter_set_id: str
    event_date: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)
