import calculator
import unittest


class TestCalculator(unittest.TestCase):

    # want write test for getNumber function but don't know how to handle variable_alias
    def test_first_input_validation(self):
        result = calculator.add
        self.assertRaises(TypeError, result, "four", 2)

    def test_second_input_validation(self):
        result = calculator.add
        self.assertRaises(TypeError, result, 4, "two")

    # not sure about that one
    def test_operator_validation(self):
        operator = calculator.getOperator
        self.assertRaises(TypeError, operator, "four")

    def test_add_method(self):
        result = calculator.add(10, 2)
        self.assertEqual(result, 12)

    def test_subtract_method(self):
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply_method(self):
        result = calculator.multiply(10, 3)
        self.assertEqual(result, 30)

    def test_divide_method(self):
        result = calculator.divide(30, 3)
        self.assertEqual(result, 10)

    # this one doesn't work :(
    def test_divide_by_zero_method(self):
        result = calculator.divide(10, 0)
        self.assertRaises(ZeroDivisionError, result)