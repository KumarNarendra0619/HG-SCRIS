"""Glacier-to-downstream receptor trace records."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ConnectivityTrace:
    source_id: str
    waterbody_id: str
    receptor_id: str | None
    path: tuple[str, ...]
    routing_method: str
    evidence_class: str = "C0"

    def to_dict(self) -> dict:
        return asdict(self)
