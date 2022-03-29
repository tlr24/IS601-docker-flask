""" This is the Calculator Class"""
from calculator.history import Calculations


class Calculator:
    """This is the calculator class"""

    @staticmethod
    def get_last_result_value():
        """ Get the result of the last calculation"""
        return Calculations.get_calculation_last_result()

    @staticmethod
    def add(values_tuple):
        """ This is the add method"""
        Calculations.add_addition_calculation(values_tuple)
        return True

    @staticmethod
    def subtract(values_tuple):
        """ This is the subtract method"""
        Calculations.add_subtraction_calculation(values_tuple)
        return True

    @staticmethod
    def multiply(values_tuple):
        """ This is the multiply method"""
        Calculations.add_multiplication_calculation(values_tuple)
        return True

    @staticmethod
    def divide(values_tuple):
        """ This is the divide method"""
        Calculations.add_division_calculation(values_tuple)
        return True
