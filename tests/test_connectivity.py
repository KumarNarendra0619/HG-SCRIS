import pytest

from hgscris.connectivity.network import build_network, downstream_nodes, shortest_downstream_path
from hgscris.connectivity.trace import ConnectivityTrace


@pytest.fixture
def network():
    nodes = [
        {"id": "G1", "type": "glacier"},
        {"id": "L1", "type": "lake"},
        {"id": "S1", "type": "stream"},
        {"id": "T1", "type": "tributary"},
        {"id": "R1", "type": "river"},
        {"id": "V1", "type": "settlement"},
    ]
    edges = [
        {"source": "G1", "target": "L1"},
        {"source": "L1", "target": "S1"},
        {"source": "S1", "target": "T1"},
        {"source": "T1", "target": "R1"},
        {"source": "R1", "target": "V1"},
    ]
    return build_network(nodes, edges)


def test_downstream_settlement(network):
    assert "V1" in downstream_nodes(network, "G1", {"settlement"})


def test_trace_path(network):
    assert shortest_downstream_path(network, "G1", "V1") == ["G1", "L1", "S1", "T1", "R1", "V1"]
    trace = ConnectivityTrace("G1", "L1", "V1", tuple(shortest_downstream_path(network, "G1", "V1")), "directed_network", "C0")
    assert trace.to_dict()["source_id"] == "G1"


def test_missing_path_rejected(network):
    with pytest.raises(ValueError):
        shortest_downstream_path(network, "V1", "G1")
