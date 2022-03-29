"""Test history calculations"""
import pytest
from calculator.history import Calculations
from calculator.calculations import Addition
# pylint: disable=line-too-long


@pytest.fixture
def clear_history_fixture():
    """A fixture that will run each time you pass it to a test to clear history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.clear_history()


def values_tuple():
    """Arranging data, creating reusable tuple for testing"""
    return 1, 2


@pytest.fixture
def setup_addition_calculation_fixture():
    """Set up an addition calculation and add it to the history"""
    Calculations.add_calculation(Addition(values_tuple()))


@pytest.fixture
def setup_second_calculation_fixture():
    """Set up another addition calculation in the history to use for testing"""
    numbers = (4, 5)
    Calculations.add_calculation(Addition(numbers))


def test_add_calculation_to_history(clear_history_fixture):
    """Testing adding a calculation to history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.add_calculation(Addition.create(values_tuple()))
    assert len(Calculations.history) == 1

def test_add_addition_calculation_to_history(clear_history_fixture):
    """Testing adding an addition calculation to history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.add_addition_calculation(values_tuple())
    assert len(Calculations.history) == 1


def test_add_subtraction_calculation_to_history(clear_history_fixture):
    """Testing adding a subtraction calculation to history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.add_subtraction_calculation(values_tuple())
    assert len(Calculations.history) == 1


def test_add_multiplication_calculation_to_history(clear_history_fixture):
    """Testing adding a subtraction calculation to history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.add_multiplication_calculation(values_tuple())
    assert len(Calculations.history) == 1


def test_add_division_calculation_to_history(clear_history_fixture):
    """Testing adding a division calculation to history"""
    # pylint: disable=redefined-outer-name,unused-argument
    Calculations.add_division_calculation(values_tuple())
    assert len(Calculations.history) == 1


def test_clear_calculations_history(clear_history_fixture):
    """Testing clearing the calculations history"""
    # pylint: disable=redefined-outer-name,unused-argument
    addition = Addition(values_tuple())
    Calculations.add_calculation(addition)
    assert len(Calculations.history) == 1
    assert Calculations.clear_history() is True
    assert Calculations.count_calculations() == 0


def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Test getting a calculation from the history"""
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 3


def test_count_calculations(clear_history_fixture):
    """Testing getting a count of the number of calculations in calculation history"""
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    for i in range(3):
        Calculations.add_calculation(Addition(values_tuple()))
    assert Calculations.count_calculations() == 3


def test_remove_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing removing a specific calculation"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.remove_calculation(0) is True
    assert Calculations.count_calculations() == 0


def test_get_calculation_last(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    addition = Addition(values_tuple())
    Calculations.add_calculation(addition)
    assert Calculations.get_calculation_last() == addition


def test_get_calculation_last_result(clear_history_fixture, setup_addition_calculation_fixture, setup_second_calculation_fixture):
    """Testing getting the result of the last calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name,line-too-long
    assert Calculations.get_calculation_last_result() == 9


def test_get_calculation_first(clear_history_fixture):
    """Testing getting the first calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    addition = Addition(values_tuple())
    addition2 = Addition(values_tuple())
    Calculations.add_calculation(addition)
    Calculations.add_calculation(addition2)
    assert Calculations.get_calculation_first() == addition


def test_get_calculation_first_result(clear_history_fixture, setup_addition_calculation_fixture, setup_second_calculation_fixture):
    """Testing getting the result of the first calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name,line-too-long
    assert Calculations.get_calculation_first_result() == 3
