"""Evidence and event-record validation primitives for HG-SCRIS."""

from __future__ import annotations

from dataclasses import dataclass


VALID_EVIDENCE = {"primary", "satellite", "remote_sensing", "government", "scientific", "news", "crowdsourced", "field", "secondary"}
VALID_CONFIDENCE = {"high", "medium", "low", "pending"}
VALID_QA = {"not_started", "pending", "passed", "failed"}


@dataclass(frozen=True)
class EventEvidence:
    evidence_id: str
    event_id: str
    evidence_type: str
    source_name: str
    source_url: str
    claim: str
    confidence: str = "pending"
    independent_source: bool = False

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.evidence_id.strip() or not self.event_id.strip():
            errors.append("evidence_id and event_id are required")
        if self.evidence_type not in VALID_EVIDENCE:
            errors.append("invalid evidence_type")
        if not self.source_name.strip() or not self.source_url.strip():
            errors.append("source_name and source_url are required")
        if not self.claim.strip():
            errors.append("claim is required")
        if self.confidence not in VALID_CONFIDENCE:
            errors.append("invalid confidence")
        return errors


def evidence_score(records: list[EventEvidence]) -> float:
    """Transparent screening score; not a statistical probability of event truth."""
    valid = [r for r in records if not r.validate()]
    if not valid:
        return 0.0
    weights = {"high": 1.0, "medium": 0.6, "low": 0.3, "pending": 0.0}
    independent = sum(1 for r in valid if r.independent_source)
    confidence = sum(weights[r.confidence] for r in valid) / len(valid)
    diversity = min(1.0, independent / 3.0)
    return round(0.7 * confidence + 0.3 * diversity, 3)
