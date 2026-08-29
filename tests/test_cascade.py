import pytest

from hgscris.hazard.cascade import CascadeEdge, build_cascade_graph, downstream_processes
from hgscris.hazard.cascade_rules import standard_process_chain


def test_glof_chain_is_candidate_not_probability():
    nodes = [
        {"id": "trigger", "type": "trigger"},
        {"id": "water", "type": "water"},
        {"id": "stream", "type": "stream"},
        {"id": "river", "type": "river"},
    ]
    graph = build_cascade_graph(nodes, standard_process_chain("GLOF"))
    assert "river" in downstream_processes(graph, "trigger")
    assert graph.edges["trigger", "water"]["evidence_class"] == "C0"


def test_unknown_node_type_rejected():
    with pytest.raises(ValueError):
        build_cascade_graph([{"id": "x", "type": "unknown"}], [])
