"""Transparent risk/impact calculations.

These functions deliberately separate hazard, exposure and vulnerability.
"""

from __future__ import annotations


def expected_loss(hazard_intensity: float, exposure_value: float, vulnerability: float, probability: float = 1.0) -> float:
    """Calculate scenario-weighted expected loss from explicit inputs."""
    for name, value in {
        "hazard_intensity": hazard_intensity,
        "exposure_value": exposure_value,
        "vulnerability": vulnerability,
        "probability": probability,
    }.items():
        if value < 0:
            raise ValueError(f"{name} cannot be negative.")
    if vulnerability > 1 or probability > 1:
        raise ValueError("vulnerability and probability must be in [0, 1].")
    return hazard_intensity * exposure_value * vulnerability * probability


def risk_class(score: float, thresholds: tuple[float, float, float] = (0.25, 0.5, 0.75)) -> str:
    """Classify a normalized screening score using explicitly supplied thresholds."""
    if not 0 <= score <= 1:
        raise ValueError("score must be in [0, 1].")
    if len(thresholds) != 3 or not (0 < thresholds[0] < thresholds[1] < thresholds[2] < 1):
        raise ValueError("thresholds must contain three ascending values in (0,1).")
    if score < thresholds[0]:
        return "low"
    if score < thresholds[1]:
        return "moderate"
    if score < thresholds[2]:
        return "high"
    return "very_high"
