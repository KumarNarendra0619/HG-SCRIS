"""Acceptance checks for the HG-SCRIS end-to-end pilot."""

from __future__ import annotations


def check_pilot_readiness(
    *,
    required_assets: dict[str, bool],
    lineage_complete: bool,
    qa_passed: bool,
    observed_validation_available: bool,
) -> dict[str, object]:
    missing = sorted(name for name, available in required_assets.items() if not available)
    gates = {
        "required_assets": not missing,
        "lineage": lineage_complete,
        "qa": qa_passed,
        "validation_evidence": observed_validation_available,
    }
    return {
        "ready": all(gates.values()),
        "gates": gates,
        "missing_assets": missing,
    }
