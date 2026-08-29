"""Conservative process-link rules used to construct cascade scenarios."""

from __future__ import annotations

from .cascade import CascadeEdge


def standard_process_chain(trigger_type: str) -> list[CascadeEdge]:
    """Return a candidate physical-process chain for a trigger class."""
    trigger = trigger_type.lower().replace("-", "_")
    if trigger in {"glof", "lake_outburst"}:
        return [
            CascadeEdge("trigger", "water", "lake_outburst", "C0"),
            CascadeEdge("water", "stream", "surface_flow", "C0"),
            CascadeEdge("stream", "river", "channel_confluence", "C0"),
        ]
    if trigger in {"debris_flow", "mass_movement"}:
        return [
            CascadeEdge("trigger", "debris", "mass_mobilisation", "C0"),
            CascadeEdge("debris", "stream", "channel_entry", "C0"),
            CascadeEdge("stream", "river", "channel_confluence", "C0"),
        ]
    if trigger in {"rock_ice_avalanche", "ice_rock_avalanche"}:
        return [
            CascadeEdge("trigger", "rock", "mass_release", "C0"),
            CascadeEdge("rock", "water", "possible_impulse_generation", "C0"),
            CascadeEdge("water", "stream", "surface_flow", "C0"),
        ]
    raise ValueError(f"Unsupported trigger type: {trigger_type}")
