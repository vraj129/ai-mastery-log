import pytest

from day10 import checked_sqrt, NegativeNumberError, safe_divide, safe_int


def test_sqrt():
    assert checked_sqrt(4) == 2.0
    assert checked_sqrt(0) == 0.0
    with pytest.raises(NegativeNumberError):
        checked_sqrt(-10)


@pytest.mark.parametrize("a,b,c", [
    (4, 2, 2.0),
    (2, 2, 1.0),
    (-2, 2, -1.0),
])
def test_divide(a, b, c):
    assert safe_divide(a, b) == c


@pytest.mark.parametrize("a,b,exception", [
    (2, 0, ZeroDivisionError)
])
def test_divide_by_zero(a, b, exception):
    with pytest.raises(exception):
        safe_divide(a, b)


def test_int():
    assert safe_int("4") == 4
    with pytest.raises(ValueError):
        safe_int("hello")
