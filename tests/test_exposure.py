import geopandas as gpd
from shapely.geometry import Point, box

from hgscris.exposure.intersect import prepare_settlements, intersect_corridor
from hgscris.exposure.metrics import summarize_exposure


def test_settlement_corridor_intersection():
    settlements = gpd.GeoDataFrame(
        {"settlement_id": ["S1", "S2"], "population": [100, 200]},
        geometry=[Point(0.5, 0.5), Point(5, 5)], crs="EPSG:4326"
    )
    corridor = gpd.GeoDataFrame(geometry=[box(0, 0, 1, 1)], crs="EPSG:4326")
    clean = prepare_settlements(settlements)
    exposed = intersect_corridor(clean, corridor)
    assert len(exposed) == 1
    summary = summarize_exposure(exposed, population_field="population")
    assert summary["population_exposed"] == 100
