"""Temporal change metrics for glacier and glacial-lake observations."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import date


@dataclass(frozen=True)
class Observation:
    entity_id: str
    observation_date: str
    value: float
    variable: str
    source: str
    uncertainty: float | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def annualized_change(start_value: float, end_value: float, start_date: str, end_date: str) -> float:
    """Return absolute change per year between two dated observations."""
    d0 = date.fromisoformat(start_date)
    d1 = date.fromisoformat(end_date)
    days = (d1 - d0).days
    if days <= 0:
        raise ValueError("end_date must be later than start_date.")
    return (end_value - start_value) / (days / 365.25)


def relative_change(start_value: float, end_value: float) -> float | None:
    """Return fractional change; None when baseline is zero."""
    if start_value == 0:
        return None
    return (end_value - start_value) / start_value
