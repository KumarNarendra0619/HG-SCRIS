"""Scenario inputs and transparent propagation calculations."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class CascadeScenario:
    scenario_id: str
    process: str
    initial_volume_m3: float
    representative_velocity_ms: float
    routing_distance_m: float
    attenuation_factor: float = 1.0

    def __post_init__(self) -> None:
        if not self.scenario_id or not self.process:
            raise ValueError("scenario_id and process are required.")
        if self.initial_volume_m3 < 0:
            raise ValueError("Initial volume cannot be negative.")
        if self.representative_velocity_ms <= 0:
            raise ValueError("Representative velocity must be positive.")
        if self.routing_distance_m < 0:
            raise ValueError("Routing distance cannot be negative.")
        if not 0 < self.attenuation_factor <= 1:
            raise ValueError("attenuation_factor must be in (0, 1].")

    def to_dict(self) -> dict:
        return asdict(self)


def travel_time_seconds(distance_m: float, velocity_ms: float) -> float:
    """Compute kinematic travel time for a prescribed representative velocity."""
    if distance_m < 0 or velocity_ms <= 0:
        raise ValueError("Distance must be non-negative and velocity positive.")
    return distance_m / velocity_ms


def attenuated_volume(initial_volume_m3: float, attenuation_factor: float) -> float:
    """Apply an explicitly prescribed scenario attenuation factor."""
    if initial_volume_m3 < 0 or not 0 < attenuation_factor <= 1:
        raise ValueError("Invalid volume or attenuation factor.")
    return initial_volume_m3 * attenuation_factor
