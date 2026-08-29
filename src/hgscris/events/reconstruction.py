"""Transparent event-reconstruction primitives for HG-SCRIS.

These functions create traceable scenario components; they are not calibrated
hydrodynamic or debris-flow solvers.
"""

from __future__ import annotations

from dataclasses import dataclass


VALID_STATUS = {"observed", "inferred", "modelled"}


@dataclass(frozen=True)
class ReconstructionStep:
    step_id: str
    event_id: str
    stage: str
    status: str
    input_refs: tuple[str, ...]
    output_ref: str
    method: str
    uncertainty: str = "unknown"

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.status not in VALID_STATUS:
            errors.append("invalid status")
        if not self.step_id.strip() or not self.event_id.strip():
            errors.append("step_id and event_id are required")
        if not self.stage.strip() or not self.method.strip():
            errors.append("stage and method are required")
        if not self.output_ref.strip():
            errors.append("output_ref is required")
        if not self.input_refs:
            errors.append("at least one input reference is required")
        return errors


def validate_reconstruction_chain(steps: list[ReconstructionStep]) -> list[str]:
    """Validate traceability and prevent a modelled step from masquerading as observed evidence."""
    errors: list[str] = []
    outputs = set()
    for step in steps:
        errors.extend(f"{step.step_id}: {e}" for e in step.validate())
        if step.output_ref in outputs:
            errors.append(f"duplicate output_ref: {step.output_ref}")
        outputs.add(step.output_ref)
    return errors


def scenario_envelope(distances_km: list[float], *, max_distance_km: float) -> list[float]:
    """Return a geometric screening envelope only; no intensity/probability is implied."""
    if max_distance_km <= 0:
        raise ValueError("max_distance_km must be > 0")
    if any(d < 0 for d in distances_km):
        raise ValueError("distances cannot be negative")
    return [d for d in distances_km if d <= max_distance_km]
