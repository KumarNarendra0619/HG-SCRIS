"""Evidence-led historical event reconstruction primitives for HG-SCRIS.

These functions keep observed, inferred and modelled evidence separate. They
are not calibrated hydrodynamic or debris-flow solvers.
"""

from __future__ import annotations

from dataclasses import dataclass

VALID_STATUS = {"observed", "inferred", "modelled"}

@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    event_id: str
    phenomenon: str
    claim_type: str
    confidence: str
    independent_source_group: str


def validate_evidence(evidence: Evidence) -> list[str]:
    errors: list[str] = []
    for field, value in {
        "evidence_id": evidence.evidence_id,
        "event_id": evidence.event_id,
        "phenomenon": evidence.phenomenon,
        "claim_type": evidence.claim_type,
        "confidence": evidence.confidence,
        "independent_source_group": evidence.independent_source_group,
    }.items():
        if not value:
            errors.append(f"{field} is required")
    return errors


def evidence_independence_count(evidence: list[Evidence]) -> int:
    return len({e.independent_source_group for e in evidence if e.independent_source_group})


def reconstruction_status(*, observed_count: int, inferred_count: int, contradicted_count: int) -> str:
    if contradicted_count > 0:
        return "CONTESTED"
    if observed_count > 0 and inferred_count > 0:
        return "OBSERVED_PLUS_INFERRED"
    if observed_count > 0:
        return "OBSERVED_SUPPORTED"
    if inferred_count > 0:
        return "INFERRED_ONLY"
    return "INSUFFICIENT_EVIDENCE"
