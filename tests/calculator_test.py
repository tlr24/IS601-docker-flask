"""Testing the Calculator"""
from calculator import Calculator


def values_tuple():
    """Creating reusable tuple for testing"""
    # Arranging data for AAA testing
    return 5, 2

def test_calculator_add_method():
    """Testing the Calculator Add method"""
    # Act for AAA testing
    result = Calculator.add(values_tuple())

    # Assertion for AAA testing
    assert result == 7

def test_calculator_subtract_method():
    """Testing the Calculator Subtract method"""
    assert Calculator.subtract(values_tuple()) == 3

def test_calculator_multiply_method():
    """Testing the Calculator Multiply method"""
    assert Calculator.multiply(values_tuple()) == 10

def test_calculator_divide_method():
    """Testing the Calculator Divide method"""
    assert Calculator.divide(values_tuple()) == 2.5
