import pytest

from hgscris.events.evidence import EventEvidence, evidence_score


def test_valid_evidence():
    e = EventEvidence("E1", "EV1", "satellite", "Source", "https://example.org", "Observed inundation", "high", True)
    assert e.validate() == []


def test_invalid_evidence_type():
    e = EventEvidence("E1", "EV1", "made_up", "Source", "https://example.org", "Claim")
    assert "invalid evidence_type" in e.validate()


def test_evidence_score_is_bounded():
    records = [EventEvidence(str(i), "EV1", "field", "S", "https://example.org", "claim", "high", True) for i in range(5)]
    assert 0 <= evidence_score(records) <= 1
