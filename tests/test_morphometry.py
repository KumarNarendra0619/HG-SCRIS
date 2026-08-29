import pytest

from hgscris.terrain.morphometry import (
    validate_dem_metadata,
    validate_derived_slope,
    valley_confinement_index,
)


def test_dem_metadata():
    assert validate_dem_metadata(horizontal_crs="EPSG:32644", vertical_datum="unknown", resolution_m=10, nodata_defined=True) == []


def test_invalid_dem_metadata():
    assert validate_dem_metadata(horizontal_crs="", vertical_datum="", resolution_m=0, nodata_defined=False)


def test_slope_range():
    assert validate_derived_slope(0, 90) == []
    assert validate_derived_slope(-1, 30)


def test_confinement_ratio():
    assert valley_confinement_index(100, 20) == pytest.approx(0.2)
