"""Testing the operations"""
from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_operations_add_method():
    """Testing the Addition Operation"""
    assert Addition.add(1, 1) == 2

def test_operations_subtract_method():
    """Testing the Subtraction Operation"""
    assert Subtraction.subtract(5, 2) == 3

def test_operations_multiply_method():
    """Testing the Multiplication Operation"""
    assert Multiplication.multiply(5, 2) == 10

def test_operations_divide_method():
    """Testing the Division Operation"""
    assert Division.divide(8, 2) == 4

def test_operations_divide_by_zero():
    """Testing the Division Operation divide by zero exception"""
    assert Division.divide(8, 0) == "Cannot divide by zero"
