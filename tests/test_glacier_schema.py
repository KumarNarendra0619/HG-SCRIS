from hgscris.glacier.schema import GlacierRecord


def base_record(**kwargs):
    data = dict(
        source_glacier_id="SRC-001",
        hgscris_glacier_id="HG-000001",
        inventory_name="test inventory",
        inventory_version="v1",
        area_km2=2.0,
        data_quality="passed",
        source_url="https://example.org/data",
        processing_version="v0.1",
        lineage_id="LIN-001",
        elevation_min_m=4000,
        elevation_max_m=5200,
        mean_slope_deg=18,
    )
    data.update(kwargs)
    return GlacierRecord(**data)


def test_valid_glacier_record():
    assert base_record().validate() == []


def test_invalid_elevation_order():
    errors = base_record(elevation_min_m=6000, elevation_max_m=5000).validate()
    assert "elevation_min_m cannot exceed elevation_max_m" in errors


def test_invalid_slope():
    errors = base_record(mean_slope_deg=95).validate()
    assert "mean_slope_deg must be between 0 and 90" in errors
