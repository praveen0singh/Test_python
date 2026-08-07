import pytest
from src import math_utils

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
])
def test_add(a, b, expected):
    assert math_utils.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (5, 0, 0),
    (-2, 3, -6),
    (1.5, 2, 3.0),
])
def test_multiply(a, b, expected):
    assert math_utils.multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5.0),
    (3, 2, 1.5),
    (-6, 3, -2.0),
])
def test_divide(a, b, expected):
    assert math_utils.divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        math_utils.divide(1, 0)
