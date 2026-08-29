import geopandas as gpd
from shapely.geometry import LineString
import pytest

from hgscris.hazard.corridor import build_channel_corridor
from hgscris.hazard.scenario import CascadeScenario


def test_corridor_requires_projected_crs():
    channel = gpd.GeoDataFrame(geometry=[LineString([(0, 0), (1, 1)])], crs="EPSG:4326")
    with pytest.raises(ValueError):
        build_channel_corridor(channel, 100)


def test_scenario_is_reproducible_descriptor():
    s = CascadeScenario("S1", "GLOF", "moderate", "channel_buffer_screening", "P1")
    assert s.to_dict()["scenario_id"] == "S1"
