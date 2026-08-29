"""Scientific-state-aware layer metadata for 2D/3D visualization."""

from __future__ import annotations

from dataclasses import dataclass, asdict

SCIENTIFIC_STATES = {"OBSERVED", "INFERRED", "MODELLED", "SCENARIO", "UNCERTAIN"}


@dataclass(frozen=True)
class LayerSpec:
    layer_id: str
    title: str
    geometry_type: str
    z_mode: str = "terrain"
    visible: bool = True
    source_version: str | None = None
    scientific_state: str = "OBSERVED"

    def __post_init__(self) -> None:
        if self.scientific_state not in SCIENTIFIC_STATES:
            raise ValueError(f"Unsupported scientific state: {self.scientific_state}")

    def to_dict(self) -> dict:
        return asdict(self)


def default_hgscris_layers() -> list[LayerSpec]:
    return [
        LayerSpec("terrain", "Terrain / DEM", "raster", scientific_state="OBSERVED"),
        LayerSpec("glaciers", "Glaciers", "polygon", scientific_state="OBSERVED"),
        LayerSpec("lakes", "Glacial Lakes", "polygon", scientific_state="OBSERVED"),
        LayerSpec("hydrography", "Streams / Rivers", "line", scientific_state="OBSERVED"),
        LayerSpec("hazard", "Modelled Hazard", "polygon", scientific_state="MODELLED"),
        LayerSpec("exposure", "Exposed Receptors", "mixed", scientific_state="OBSERVED"),
        LayerSpec("evacuation", "Evacuation Routes", "line", scientific_state="MODELLED"),
        LayerSpec("safe_zones", "Candidate Safe Zones", "polygon", scientific_state="INFERRED"),
    ]


def validate_layer_states(layers: list[LayerSpec]) -> list[str]:
    """Return deterministic validation errors for scientific visualization state."""
    errors: list[str] = []
    for layer in layers:
        if layer.scientific_state not in SCIENTIFIC_STATES:
            errors.append(f"{layer.layer_id}: invalid scientific_state")
        if layer.scientific_state in {"MODELLED", "SCENARIO", "INFERRED", "UNCERTAIN"} and not layer.source_version:
            errors.append(f"{layer.layer_id}: non-observed layer requires source_version")
    return errors
