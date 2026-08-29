"""Transparent trigger-screening scores for scenario prioritisation.

The score is a prioritisation index, not a probability of GLOF or other failure.
Weights are explicit and must be calibrated/validated before scientific use.
"""

from __future__ import annotations


def weighted_trigger_index(factors: dict[str, float], weights: dict[str, float]) -> float:
    """Compute a weighted index from normalized 0..1 factors."""
    if not factors:
        raise ValueError("At least one factor is required.")
    if set(factors) != set(weights):
        raise ValueError("Factors and weights must have identical keys.")
    if any(not 0 <= float(v) <= 1 for v in factors.values()):
        raise ValueError("Factors must be normalized to [0, 1].")
    if any(float(w) < 0 for w in weights.values()):
        raise ValueError("Weights cannot be negative.")
    total = sum(float(w) for w in weights.values())
    if total <= 0:
        raise ValueError("Weight sum must be positive.")
    return sum(float(factors[k]) * float(weights[k]) for k in factors) / total


def classify_screening_index(index: float) -> str:
    """Classify a screening index; labels are prioritisation classes only."""
    if not 0 <= index <= 1:
        raise ValueError("Index must be in [0, 1].")
    if index < 0.25:
        return "low"
    if index < 0.50:
        return "moderate"
    if index < 0.75:
        return "high"
    return "very_high"
