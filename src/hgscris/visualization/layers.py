"""Layer metadata for 2D/3D research visualization."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class LayerSpec:
    layer_id: str
    title: str
    geometry_type: str
    z_mode: str = "terrain"
    visible: bool = True
    source_version: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def default_hgscris_layers() -> list[LayerSpec]:
    return [
        LayerSpec("terrain", "Terrain / DEM", "raster", "terrain"),
        LayerSpec("glaciers", "Glaciers", "polygon", "terrain"),
        LayerSpec("lakes", "Glacial Lakes", "polygon", "terrain"),
        LayerSpec("hydrography", "Streams / Rivers", "line", "terrain"),
        LayerSpec("hazard", "Modelled Hazard", "polygon", "terrain"),
        LayerSpec("exposure", "Exposed Receptors", "mixed", "terrain"),
        LayerSpec("evacuation", "Evacuation Routes", "line", "terrain"),
        LayerSpec("safe_zones", "Candidate Safe Zones", "polygon", "terrain"),
    ]
