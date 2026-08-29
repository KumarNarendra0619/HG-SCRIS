import pytest

from hgscris.exposure.linkage import ExposureRecord, corridor_distance, classify_screening_band


def test_exposure_validation():
    e = ExposureRecord("E1", "settlement", 10, 20, "SRC1", "passed")
    assert e.validate() == []


def test_corridor_distance():
    e = ExposureRecord("E1", "settlement", 10, 20, "SRC1", "passed")
    assert corridor_distance(e, [(0, 20), (10, 20)]) == pytest.approx(0)


def test_screening_band():
    assert classify_screening_band(50, (100, 500)) == "near_corridor"
    assert classify_screening_band(300, (100, 500)) == "intermediate_corridor"
    assert classify_screening_band(600, (100, 500)) == "outside_screening_corridor"
