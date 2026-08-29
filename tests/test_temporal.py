import pandas as pd
import pytest

from hgscris.temporal.change import annualized_change, relative_change
from hgscris.temporal.series import validate_series, change_table


def test_annualized_change():
    value = annualized_change(100, 110, "2020-01-01", "2021-01-01")
    assert value == pytest.approx(10.0, rel=0.01)


def test_relative_zero_is_unknown():
    assert relative_change(0, 10) is None


def test_series_change_table():
    df = pd.DataFrame([
        {"entity_id": "G1", "observation_date": "2020-01-01", "value": 100, "variable": "area", "source": "A"},
        {"entity_id": "G1", "observation_date": "2025-01-01", "value": 90, "variable": "area", "source": "B"},
    ])
    out = change_table(validate_series(df))
    assert out.loc[0, "absolute_change"] == -10
    assert out.loc[0, "relative_change"] == pytest.approx(-0.1)
