"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator Add method"""
    values_tuple = (1, 1)
    assert Calculator.add(values_tuple) == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract method"""
    values_tuple = (5, 2)
    assert Calculator.subtract(values_tuple) == 3

def test_calculator_multiply_method():
    """Testing the Calculator Multiply method"""
    values_tuple = (5, 2)
    assert Calculator.multiply(values_tuple) == 10

def test_calculator_divide_method():
    """Testing the Calculator Divide method"""
    values_tuple = (8, 2)
    assert Calculator.divide(values_tuple) == 4
