"""Includes classes for all calculator operations"""


class Addition:
    """Class for addition operation"""

    @staticmethod
    def add(value_1, value_2):
        """Adds two numbers together"""
        return value_1 + value_2


class Subtraction:
    """Class for subtraction operation"""

    @staticmethod
    def subtract(value_1, value_2):
        """Subtracts two numbers together"""
        return value_1 - value_2


class Multiplication:
    """Class for multiplication operation"""

    @staticmethod
    def multiply(value_1, value_2):
        """Multiplies two numbers together"""
        return value_1 * value_2


class Division:
    """Class for division operation"""

    @staticmethod
    def divide(value_1, value_2):
        """Divides two numbers"""
        try:
            return value_1 / value_2
        except ZeroDivisionError:
            return "Cannot divide by zero"
