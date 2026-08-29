from hgscris.forcing.validation import classify_temporal_match, validate_forcing_record


def test_forcing_record_validation():
    errors = validate_forcing_record(variable="", units="", time_start="", time_end="", time_step="")
    assert len(errors) == 4


def test_temporal_match():
    assert classify_temporal_match("2020-07-15", "2020-01-01", "2020-12-31") == "COVERED"
    assert classify_temporal_match("2021-01-01", "2020-01-01", "2020-12-31") == "OUTSIDE_COVERAGE"
