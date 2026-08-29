import numpy as np
import pytest

from hgscris.terrain.morphology import slope_degrees, longitudinal_gradient, normalized_relief


def test_slope_degrees():
    out = slope_degrees(np.array([0.0, 1.0]), np.array([0.0, 0.0]))
    assert out[1] == pytest.approx(45.0)


def test_longitudinal_gradient():
    assert longitudinal_gradient(4500, 3500, 10000) == pytest.approx(0.1)


def test_relief():
    assert normalized_relief(np.array([100, 120, 150])) == 50
