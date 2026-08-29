from hgscris.pilot.acceptance import check_pilot_readiness


def test_pilot_not_ready_with_missing_assets():
    result = check_pilot_readiness(
        required_assets={"dem": True, "hydrography": False},
        lineage_complete=True,
        qa_passed=True,
        observed_validation_available=True,
    )
    assert result["ready"] is False
    assert result["missing_assets"] == ["hydrography"]


def test_pilot_ready_when_all_gates_pass():
    result = check_pilot_readiness(
        required_assets={"dem": True, "hydrography": True, "exposure": True},
        lineage_complete=True,
        qa_passed=True,
        observed_validation_available=True,
    )
    assert result["ready"] is True
