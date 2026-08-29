"""Hazard scenario definitions and validation for HG-SCRIS."""

from __future__ import annotations

from dataclasses import dataclass, asdict

ALLOWED_PROCESSES = {
    "GLOF", "FLUVIAL_FLOOD", "DEBRIS_FLOW", "LANDSLIDE_RUNOUT",
    "AVALANCHE", "ICEFALL", "COMPOUND_CASCADE",
}


@dataclass(frozen=True)
class CascadeScenario:
    """A reproducible process-specific hazard scenario descriptor."""
    scenario_id: str
    trigger_type: str
    forcing_class: str
    corridor_method: str
    parameter_set_id: str
    event_date: str | None = None
    hazard_process: str = "COMPOUND_CASCADE"

    def to_dict(self) -> dict:
        return asdict(self)


def validate_scenario(*, scenario_id: str, hazard_process: str, source_type: str) -> list[str]:
    errors: list[str] = []
    if not scenario_id:
        errors.append("scenario_id is required")
    if hazard_process not in ALLOWED_PROCESSES:
        errors.append("unsupported hazard_process")
    if source_type not in {"OBSERVED", "INFERRED", "MODELLED"}:
        errors.append("source_type must be OBSERVED, INFERRED or MODELLED")
    return errors


def classify_result(source_type: str, validation_status: str) -> str:
    """Keep observed, modelled and unvalidated states distinct."""
    if source_type == "OBSERVED" and validation_status == "VALIDATED":
        return "OBSERVED_HAZARD"
    if source_type == "MODELLED" and validation_status == "VALIDATED":
        return "MODELLED_SCENARIO"
    return "UNVALIDATED_SCENARIO"
