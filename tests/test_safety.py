import networkx as nx
import pytest

from hgscris.safety.routing import shortest_safe_route, route_travel_time
from hgscris.safety.suitability import safe_zone_screen


def test_shortest_safe_route():
    g = nx.Graph()
    g.add_edge("A", "B", travel_time_s=10)
    g.add_edge("B", "SAFE", travel_time_s=20)
    g.add_edge("A", "C", travel_time_s=5)
    g.add_edge("C", "SAFE", travel_time_s=50)
    path = shortest_safe_route(g, "A", {"SAFE"})
    assert path == ["A", "B", "SAFE"]
    assert route_travel_time(g, path) == 30


def test_blocked_route():
    g = nx.Graph()
    g.add_edge("A", "B", travel_time_s=10)
    g.add_edge("B", "SAFE", travel_time_s=10)
    with pytest.raises(ValueError):
        shortest_safe_route(g, "A", {"SAFE"}, {"B"})


def test_safe_zone_screen():
    result = safe_zone_screen(True, True, 300, 100, 80)
    assert result["eligible_screening"] is True
