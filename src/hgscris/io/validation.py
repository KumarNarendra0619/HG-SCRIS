"""Validation helpers for ingestion outputs."""

from __future__ import annotations

from collections.abc import Iterable


def require_columns(columns: Iterable[str], required: Iterable[str]) -> list[str]:
    """Return required columns that are missing from an input schema."""
    available = set(columns)
    return [name for name in required if name not in available]


def validate_required_columns(columns: Iterable[str], required: Iterable[str]) -> None:
    """Raise ValueError when required schema fields are absent."""
    missing = require_columns(columns, required)
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
