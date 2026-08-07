"""Small math utilities for examples and tests.

Simple functions: add, multiply, divide.
"""
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return a divided by b. Let Python raise ZeroDivisionError for b == 0."""
    return a / b
