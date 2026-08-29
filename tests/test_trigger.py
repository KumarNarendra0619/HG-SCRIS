import pytest

from hgscris.trigger.lake_metrics import LakeMetrics, validate_lake_metrics
from hgscris.trigger.screening import weighted_trigger_index, classify_screening_index


def test_lake_metrics_validation():
    m = LakeMetrics("L1", 1000, elevation_m=4500, volume_m3=100000)
    assert validate_lake_metrics(m).lake_id == "L1"


def test_weighted_index():
    idx = weighted_trigger_index({"area": 1.0, "slope": 0.5}, {"area": 1, "slope": 1})
    assert idx == pytest.approx(0.75)
    assert classify_screening_index(idx) == "very_high"


def test_invalid_factor():
    with pytest.raises(ValueError):
        weighted_trigger_index({"area": 2}, {"area": 1})
