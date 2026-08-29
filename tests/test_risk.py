import pytest

from hgscris.risk.model import expected_loss, risk_class


def test_expected_loss():
    assert expected_loss(0.8, 100, 0.5, 0.5) == 20


def test_risk_class():
    assert risk_class(0.1) == "low"
    assert risk_class(0.9) == "very_high"


def test_invalid_probability():
    with pytest.raises(ValueError):
        expected_loss(1, 100, 0.5, 1.2)
