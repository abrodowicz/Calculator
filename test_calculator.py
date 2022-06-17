import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.x = 10
        self.y = 2
        self.calc = calculator.calculate()
        print("SETUP called")

    def tearDown(self):
        self.x = 0
        self.y = 0
        print("TEARDOWN called")

    def test_add_method(self):
        self.x = 10
        self.y = 2
        result = self.calc.add(self.x, self.y)
        self.assertEqual(result, self.x + self.y)

    #
    # def test_add_method_invalid_value(self):
    #     self.assertRaises(ValueError, self.calculator.add, "four", "five")

    def test_multiply_method(self):
        result = self.calc.multiply(self.x, self.y)
        self.assertEqual(result, self.x * self.y)

    # def test_multiply_method_invalid_value(self):
    #     self.assertRaises(ValueError, self.calculator.multiply, "four", "five")

    def test_subtract_method(self):
        result = self.calc.subtract(self.x, self.y)
        self.assertEqual(result, self.x - self.y)
    #
    # def test_sub_method_invalid_value(self):
    #     self.assertRaises(ValueError, self.calculator.sub, "four", "five")

    def test_divide_method(self):
        result = self.calc.divide(self.x, self.y)
        self.assertEqual(result, self.x / self.y)
    #
    # def test_div_method_invalid_value(self):
    #     self.assertRaises(ValueError, self.calculator.div, "five", "four")
    #
    # def test_div_method_zero(self):
    #     self.assertRaises(ZeroDivisionError, self.calculator.div, 5, 0)


if __name__ == '__main__':
    unittest.main()
