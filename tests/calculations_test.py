"""Tests the Calculations class and Calculation Operation classes"""
from calculator.calculations import Addition, Subtraction, Multiplication, Division


def values_tuple():
    """Arranging data, creating reusable tuple for testing"""
    return 4, 2

def test_addition_instance():
    """Tests that an addition calculation can be instantiated"""
    addition_object = Addition.create(values_tuple())
    assert isinstance(addition_object, Addition)

def test_subtraction_instance():
    """Tests that a subtraction calculation can be instantiated"""
    subtraction_object = Subtraction.create(values_tuple())
    assert isinstance(subtraction_object, Subtraction)

def test_multiplication_instance():
    """Tests that a multiplication calculation can be instantiated"""
    multiplication_object = Multiplication.create(values_tuple())
    assert isinstance(multiplication_object, Multiplication)

def test_division_instance():
    """Tests that a division calculation can be instantiated"""
    division_object = Division.create(values_tuple())
    assert isinstance(division_object, Division)

def test_addition_get_result():
    """Tests the addition calculation get_result method"""
    addition_object = Addition.create(values_tuple())
    assert addition_object.get_result() == 6

def test_subtraction_get_result():
    """Tests the subtraction calculation get_result method"""
    subtraction_object = Subtraction.create(values_tuple())
    assert subtraction_object.get_result() == 2

def test_multiplication_get_result():
    """Tests the multiplication calculation get_result method"""
    multiplication_object = Multiplication.create(values_tuple())
    assert multiplication_object.get_result() == 8

def test_division_get_result():
    """Tests the division calculation get_result method"""
    division_object = Division.create(values_tuple())
    assert division_object.get_result() == 2
