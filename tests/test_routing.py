import numpy as np

from hgscris.hydrology.routing import d8_flow_direction, flow_accumulation
from hgscris.hydrology.graph import routing_graph, downstream_path


def test_d8_and_accumulation():
    dem = np.array([[5, 4, 3], [6, 5, 2], [7, 6, 1]], dtype=float)
    fd = d8_flow_direction(dem)
    acc = flow_accumulation(fd)
    assert acc.shape == dem.shape
    assert acc[2, 2] >= 3


def test_graph_downstream_path():
    fd = np.array([[4, 4], [4, -1]], dtype=np.int8)
    graph = routing_graph(fd)
    path = downstream_path(graph, (0, 0))
    assert path[-1] == (1, 1)
