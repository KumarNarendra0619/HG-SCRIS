import numpy as np
import pytest

from hgscris.remote.catalog import SceneRecord, select_scenes
from hgscris.remote.qc import validate_raster_array


def test_scene_filter():
    scenes = [
        SceneRecord("S1", "2025-01-01", "OPTICAL", 0.10),
        SceneRecord("S2", "2025-01-02", "OPTICAL", 0.60),
    ]
    assert [s.scene_id for s in select_scenes(scenes, 0.30)] == ["S1"]


def test_scene_cloud_range():
    with pytest.raises(ValueError):
        select_scenes([SceneRecord("S1", "2025-01-01", "OPTICAL", 1.2)])


def test_raster_qc():
    out = validate_raster_array(np.array([[1.0, np.nan], [3.0, 4.0]]))
    assert out["rows"] == 2
    assert out["finite_fraction"] == 0.75
