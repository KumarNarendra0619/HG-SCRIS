import geopandas as gpd
from shapely.geometry import Polygon

from hgscris.glacier.qa import glacier_qa_report


def test_glacier_qa_clean_record():
    gdf = gpd.GeoDataFrame(
        {
            "rgi_id": ["RGI_TEST_001"],
            "area_km2": [10.0],
            "elevation_min_m": [4000.0],
            "elevation_max_m": [6000.0],
            "elevation_mean_m": [5000.0],
        },
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])],
        crs="EPSG:4326",
    )
    report = glacier_qa_report(gdf)
    assert report["records"] == 1
    assert report["missing_rgi_id"] == 0
    assert report["invalid_elevation_order"] == 0
