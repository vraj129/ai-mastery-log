import pytest

from day10 import checked_sqrt, NegativeNumberError


def test_sqrt():
    assert checked_sqrt(4) == 2.0
    assert checked_sqrt(0) == 0.0
    with pytest.raises(NegativeNumberError):
        checked_sqrt(-10)
