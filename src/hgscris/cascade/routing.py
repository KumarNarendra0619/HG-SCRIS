"""Segment-wise cascade routing over an existing directed pathway."""

from __future__ import annotations


def route_volume(initial_volume_m3: float, segment_factors: list[float]) -> list[float]:
    """Propagate a scenario volume through prescribed segment retention factors.

    This is a transparent screening/routing primitive, not a hydraulic solver.
    """
    if initial_volume_m3 < 0:
        raise ValueError("Initial volume cannot be negative.")
    volume = initial_volume_m3
    outputs = []
    for factor in segment_factors:
        if not 0 < factor <= 1:
            raise ValueError("Segment factors must be in (0, 1].")
        volume *= factor
        outputs.append(volume)
    return outputs


def arrival_times(segment_distances_m: list[float], velocities_ms: list[float]) -> list[float]:
    """Return cumulative travel time for prescribed segment velocities."""
    if len(segment_distances_m) != len(velocities_ms):
        raise ValueError("Distances and velocities must have equal length.")
    elapsed = 0.0
    out = []
    for distance, velocity in zip(segment_distances_m, velocities_ms):
        if distance < 0 or velocity <= 0:
            raise ValueError("Distances must be non-negative and velocities positive.")
        elapsed += distance / velocity
        out.append(elapsed)
    return out
