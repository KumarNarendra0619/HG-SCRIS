from hgscris.hydrography.network import downstream_chain, validate_reach


def test_downstream_chain():
    graph = {"A": "B", "B": "C", "C": None}
    assert downstream_chain(graph, "A") == ["A", "B", "C"]


def test_cycle_detection():
    graph = {"A": "B", "B": "A"}
    try:
        downstream_chain(graph, "A")
    except ValueError as exc:
        assert "cycle detected" in str(exc)
    else:
        raise AssertionError("cycle should be rejected")


def test_reach_validation():
    errors = validate_reach(reach_id="A", length_m=0, upstream_id=None, downstream_id="A")
    assert len(errors) == 2
