import pytest

from day10 import checked_sqrt, NegativeNumberError, safe_divide, safe_int


def test_sqrt():
    assert checked_sqrt(4) == 2.0
    assert checked_sqrt(0) == 0.0
    with pytest.raises(NegativeNumberError):
        checked_sqrt(-10)


def test_divide():
    assert safe_divide(4, 2) == 2.0
    with pytest.raises(ZeroDivisionError):
        safe_divide(4, 0)


def test_int():
    assert safe_int("4") == 4
    with pytest.raises(ValueError):
        safe_int("hello")
