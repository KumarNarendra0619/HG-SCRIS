"""Remote-sensing scene metadata contracts and deterministic filtering."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class SceneRecord:
    scene_id: str
    acquisition_date: str
    product: str
    cloud_fraction: float | None = None
    source: str | None = None
    processing_level: str | None = None
    asset_uri: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def validate_scene(scene: SceneRecord) -> SceneRecord:
    if not scene.scene_id or not scene.acquisition_date or not scene.product:
        raise ValueError("scene_id, acquisition_date and product are required.")
    if scene.cloud_fraction is not None and not 0 <= scene.cloud_fraction <= 1:
        raise ValueError("cloud_fraction must be in [0, 1].")
    return scene


def select_scenes(scenes: list[SceneRecord], max_cloud_fraction: float = 1.0) -> list[SceneRecord]:
    """Deterministically select scenes at or below a cloud threshold."""
    if not 0 <= max_cloud_fraction <= 1:
        raise ValueError("max_cloud_fraction must be in [0, 1].")
    validated = [validate_scene(s) for s in scenes]
    return [s for s in validated if s.cloud_fraction is None or s.cloud_fraction <= max_cloud_fraction]
