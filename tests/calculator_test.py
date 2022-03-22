"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing that we can create an instance of the calculator class"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing that we can get the result of the calculator using the get result method"""
    calculator = Calculator()
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing that the calculator stores result property in independent calculator instances"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator Add method"""
    calculator = Calculator()
    assert calculator.add(1, 1) == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract method"""
    calculator = Calculator()
    assert calculator.subtract(5, 2) == 3

def test_calculator_multiply_method():
    """Testing the Calculator Multiply method"""
    calculator = Calculator()
    assert calculator.multiply(5, 2) == 10

def test_calculator_divide_method():
    """Testing the Calculator Divide method"""
    calculator = Calculator()
    assert calculator.divide(8, 2) == 4
