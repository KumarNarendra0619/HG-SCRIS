from hgscris.terrain.metrics_v1 import relief, slope_degrees, validate_terrain_record


def test_slope_zero():
    assert slope_degrees(0, 0) == 0


def test_relief():
    assert relief(1000, 2500) == 1500


def test_invalid_terrain_record():
    errors = validate_terrain_record(cell_size_m=0, elevation_min_m=2000, elevation_max_m=1000)
    assert len(errors) == 2
