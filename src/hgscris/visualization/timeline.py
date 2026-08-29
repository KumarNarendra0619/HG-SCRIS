"""Time-slice utilities for reproducible event animation."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class AnimationFrame:
    timestamp_s: float
    hazard_extent: float | None = None
    arrival_count: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


def build_timeline(timestamps_s: list[float]) -> list[AnimationFrame]:
    """Build validated monotonically increasing animation frames."""
    if any(t < 0 for t in timestamps_s):
        raise ValueError("Timestamps cannot be negative.")
    if any(b < a for a, b in zip(timestamps_s, timestamps_s[1:])):
        raise ValueError("Timestamps must be monotonically increasing.")
    return [AnimationFrame(t) for t in timestamps_s]
