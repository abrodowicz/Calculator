import calculator
import unittest


class TestCalculator(unittest.TestCase):

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