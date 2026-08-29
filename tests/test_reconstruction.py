from hgscris.events.reconstruction import ReconstructionStep, validate_reconstruction_chain


def test_reconstruction_chain():
    steps = [
        ReconstructionStep("S1", "EV1", "source", "observed", ("SRC1",), "OBS1", "document review", "high"),
        ReconstructionStep("S2", "EV1", "flow_path", "inferred", ("OBS1",), "INF1", "DEM + hydrography", "medium"),
        ReconstructionStep("S3", "EV1", "scenario", "modelled", ("INF1",), "MOD1", "scenario routing", "medium"),
    ]
    assert validate_reconstruction_chain(steps) == []


def test_invalid_status_is_caught():
    step = ReconstructionStep("S1", "EV1", "source", "forecast", ("SRC1",), "OUT1", "method")
    assert "S1: invalid status" in validate_reconstruction_chain([step])
