"""Test history calculations"""
import pytest
from calculator.history import Calculations
from calculator.calculations import Addition


@pytest.fixture
def clear_history_fixture():
    """A fixture that will run each time you pass it to a test to clear history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.clear_history()


def values_tuple():
    """Arranging data, creating reusable tuple for testing"""
    return 1, 2


def test_add_addition_calculation_to_history():
    """Testing adding a calculation to history"""
    Calculations.add_addition_calculation(values_tuple())
    assert len(Calculations.history) == 1


def test_add_subtraction_calculation_to_history():
    """Testing adding a subtraction calculation to history"""
    Calculations.add_subtraction_calculation(values_tuple())
    assert len(Calculations.history) == 2


def test_add_multiplication_calculation_to_history():
    """Testing adding a subtraction calculation to history"""
    Calculations.add_multiplication_calculation(values_tuple())
    assert len(Calculations.history) == 3


def test_add_division_calculation_to_history():
    """Testing adding a division calculation to history"""
    Calculations.add_division_calculation(values_tuple())
    assert len(Calculations.history) == 4


def test_clear_calculations_history():
    """Testing clearing the calculations history"""
    addition = Addition(values_tuple())
    Calculations.history.append(addition)
    assert len(Calculations.history) == 5
    assert Calculations.clear_history() is True


def test_get_calculation():
    """Test getting a calculation from the history"""
    addition = Addition(values_tuple())
    Calculations.history.append(addition)
    assert Calculations.get_calculation(0).get_result() == 3


def test_count_calculations(clear_history_fixture):
    """Testing getting a count of the number of calculations in calculation history"""
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    for i in range(3):
        Calculations.history.append(Addition(values_tuple()))
    assert Calculations.count_calculations() == 3


def test_remove_calculation(clear_history_fixture):
    """Testing removing a specific calculation"""
    # pylint: disable=unused-argument,redefined-outer-name
    addition = Addition(values_tuple())
    Calculations.history.append(addition)
    assert Calculations.remove_calculation(0) is True


def test_get_calculation_last(clear_history_fixture):
    """Testing getting the last calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_last() == addition2


def test_get_calculation_last_result(clear_history_fixture):
    """Testing getting the result of the last calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_last_result() == 9


def test_get_calculation_first(clear_history_fixture):
    """Testing getting the first calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_first() == addition


def test_get_calculation_first_result(clear_history_fixture):
    """Testing getting the result of the first calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_first_result() == 3
