""" This is the Calculator Class"""
from calculator.calculations import Addition, Subtraction, Multiplication, Division


class Calculator:
    """This is the calculator class"""
    @staticmethod
    def add(values_tuple):
        """ This is the add method"""
        return Addition.create(values_tuple).get_result()

    @staticmethod
    def subtract(values_tuple):
        """ This is the subtract method"""
        return Subtraction.create(values_tuple).get_result()

    @staticmethod
    def multiply(values_tuple):
        """ This is the multiply method"""
        return Multiplication.create(values_tuple).get_result()

    @staticmethod
    def divide(values_tuple):
        """ This is the divide method"""
        return Division.create(values_tuple).get_result()
