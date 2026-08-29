import geopandas as gpd
import pytest
from shapely.geometry import Polygon

from hgscris.extraction.geometry import validate_polygons, add_area
from hgscris.extraction.change import area_change


def test_polygon_validation_and_area():
    layer = gpd.GeoDataFrame({"glacier_id": ["G1"]}, geometry=[Polygon([(0,0),(10,0),(10,10),(0,10)])], crs="EPSG:32644")
    clean = validate_polygons(layer, "glacier_id")
    out = add_area(clean)
    assert out.loc[0, "area_m2"] == 100


def test_geographic_area_rejected():
    layer = gpd.GeoDataFrame({"lake_id": ["L1"]}, geometry=[Polygon([(0,0),(1,0),(1,1),(0,1)])], crs="EPSG:4326")
    with pytest.raises(ValueError):
        add_area(layer)


def test_area_change():
    out = area_change(100, 75)
    assert out["absolute_change_m2"] == -25
    assert out["relative_change"] == pytest.approx(-0.25)
