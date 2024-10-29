import pytest
from calculator_bundle.adder import add

def test_add_positive_numbers():
    assert add(2, 3) == 5, "Adding 2 and 3 should return 5"

def test_add_negative_numbers():
    assert add(-2, -3) == -5, "Adding -2 and -3 should return -5"

def test_add_positive_and_negative():
    assert add(5, -3) == 2, "Adding 5 and -3 should return 2"

def test_add_zero():
    assert add(0, 0) == 0, "Adding 0 and 0 should return 0"
    assert add(5, 0) == 5, "Adding 5 and 0 should return 5"
    assert add(0, -3) == -3, "Adding 0 and -3 should return -3"
