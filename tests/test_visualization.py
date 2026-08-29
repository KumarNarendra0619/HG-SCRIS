import pytest

from hgscris.visualization.layers import default_hgscris_layers
from hgscris.visualization.timeline import build_timeline


def test_timeline_is_monotonic():
    frames = build_timeline([0, 60, 120])
    assert [f.timestamp_s for f in frames] == [0, 60, 120]


def test_non_monotonic_rejected():
    with pytest.raises(ValueError):
        build_timeline([0, 120, 60])


def test_default_layers():
    ids = {layer.layer_id for layer in default_hgscris_layers()}
    assert {"terrain", "glaciers", "lakes", "hydrography", "hazard", "exposure", "evacuation", "safe_zones"} <= ids
