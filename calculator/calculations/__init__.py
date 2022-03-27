""" Includes Calculation class and Calculation Operation objects"""
from calculator.operations import Addition as Add, Subtraction as Subt, Multiplication as Mult, Division as Div


class Calculation:
    """Calculation base class"""

    def __init__(self, tuple_list: tuple):
        """Constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """Factory method to create calculation objects"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """Standardize values to list of floats"""
        # lists can be modified and tuple cannot, tuple are faster.
        # We need to convert the tuple of potentially random data types (its raw data)
        # into a standard data format to keep things consistent, so we convert it to float
        # then I make it a tuple again because I actually won't need to change the calculation values
        # I can also use it as a list, and then I would be able to edit the calculation
        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)

class Addition(Calculation):
    """Class for addition calculation objects"""

    def get_result(self):
        """Get result of addition calculation"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = Add.add(value, sum_of_values)
        return sum_of_values

class Subtraction(Calculation):
    """Class for subtraction calculation objects"""

    def get_result(self):
        """Get result of subtraction calculation"""
        difference = self.values[0]
        for value in self.values[1:]:
            difference = Subt.subtract(difference, value)
        return difference

class Multiplication(Calculation):
    """Class for multiplication calculation objects"""

    def get_result(self):
        """Get result of multiplication calculation"""
        product = 1.0
        for value in self.values:
            product = Mult.multiply(value, product)
        return product

class Division(Calculation):
    """Class for division calculation objects"""

    def get_result(self):
        """Get result of division calculation"""
        quotient = self.values[0]
        for value in self.values[1:]:
            quotient = Div.divide(quotient, value)
        return quotient
