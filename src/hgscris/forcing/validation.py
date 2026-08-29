"""Validation primitives for HG-SCRIS climate/hydrological forcing."""

from __future__ import annotations


def validate_forcing_record(*, variable: str, units: str, time_start: str, time_end: str, time_step: str) -> list[str]:
    errors: list[str] = []
    if not variable:
        errors.append("variable is required")
    if not units:
        errors.append("units are required")
    if not time_start or not time_end:
        errors.append("time_start and time_end are required")
    if not time_step:
        errors.append("time_step is required")
    return errors


def classify_temporal_match(event_date: str, forcing_start: str, forcing_end: str) -> str:
    """Classify whether forcing coverage contains an event date.

    Inputs are ISO date strings (YYYY-MM-DD). This deliberately does not
    assess spatial representativeness or causal attribution.
    """
    if forcing_start <= event_date <= forcing_end:
        return "COVERED"
    return "OUTSIDE_COVERAGE"
