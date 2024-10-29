import pytest
from calculator_bundle.multiplier import multiply

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6, "Multiplying 2 and 3 should return 6"

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6, "Multiplying -2 and -3 should return 6"

def test_multiply_positive_and_negative():
    assert multiply(5, -3) == -15, "Multiplying 5 and -3 should return -15"

def test_multiply_with_zero():
    assert multiply(0, 0) == 0, "Multiplying 0 and 0 should return 0"
    assert multiply(5, 0) == 0, "Multiplying 0 and 0 should return 0"
