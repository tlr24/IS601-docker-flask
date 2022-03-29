"""Testing the Calculator"""
from calculator import Calculator


def values_tuple():
    """Creating reusable tuple for testing"""
    # Arranging data for AAA testing
    return 5, 2

def test_calculator_add_method():
    """Testing the Calculator Add method"""
    # Act for AAA testing
    Calculator.add(values_tuple())

    # Assertion for AAA testing
    assert Calculator.get_last_result_value() == 7

def test_calculator_subtract_method():
    """Testing the Calculator Subtract method"""
    Calculator.subtract(values_tuple())
    assert Calculator.get_last_result_value() == 3

def test_calculator_multiply_method():
    """Testing the Calculator Multiply method"""
    Calculator.multiply(values_tuple())
    assert Calculator.get_last_result_value() == 10

def test_calculator_divide_method():
    """Testing the Calculator Divide method"""
    Calculator.divide(values_tuple())
    assert Calculator.get_last_result_value() == 2.5
