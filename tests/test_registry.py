import pytest

from hgscris.data.registry import DatasetRecord, assert_registry_headers, REQUIRED_FIELDS


def test_required_headers():
    assert_registry_headers(list(REQUIRED_FIELDS) + ["notes"])


def test_missing_header_rejected():
    with pytest.raises(ValueError):
        assert_registry_headers(["dataset_id"])


def test_record_validation():
    record = DatasetRecord(
        "D1", "terrain", "provider", "DEM", "pilot", "2020", "10m",
        "EPSG:4326", "unknown", "https://example.org", "open", "2026-01-01",
        "v1", "passed"
    )
    assert record.validate_identity() == []
