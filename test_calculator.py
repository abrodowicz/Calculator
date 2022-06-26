import calculator
import unittest


class TestCalculator(unittest.TestCase):

    #Check if calculator greet an user/ doesn't work :(
    def test_greeting_display(self):
        greeting = calculator.welcome
        self.assertEqual(greeting, "Hello! This is your calculator.")

    #Check if calculator provide an instruction
    ?

    # Check input validation -> want to write a test for getNumber function but don't know how to handle variable_alias
    ?

    #Check operator validation- positive scenario
    ?

    #Check operator validation- negative scenario
    ?

    #Check the addition of two positive integers- positive scenario
    def test_add_method_1(self):
        result = calculator.add(10, 2)
        self.assertEqual(result, 12)

    #Check the addition of two negative integers- positive scenario
    def test_add_method_2(self):
        result = calculator.add(-10, -2)
        self.assertEqual(result, -12)

    #Check the addition of one positive and one negative integer- positive scenario
    def test_add_method_3(self):
        result = calculator.add(2, -10)
        self.assertEqual(result, -8)

    #Check the addition of two integers- negative scenario
    def test_add_method_4(self):
        result = calculator.add(-2, 10)
        self.assertNotEqual(result, 10)

    #Check the subtraction of two positive integers- positive scenario
    def test_subtract_method_1(self):
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    #Check the subtraction of two negative integers- positive scenario
    def test_subtract_method_2(self):
        result = calculator.subtract(-10, -5)
        self.assertEqual(result, -5)

    #Check the subtraction of one positive and one negative integer- positive scenario
    def test_subtract_method_3(self):
        result = calculator.subtract(10, -5)
        self.assertEqual(result, 15)

    #Check the subtraction of two integers- negative scenario
    def test_subtract_method_4(self):
        result = calculator.subtract(10, -5)
        self.assertNotEqual(result, 5)

    #Check the multiplication of two positive integers- positive scenario
    def test_multiply_method_1(self):
        result = calculator.multiply(10, 3)
        self.assertEqual(result, 30)

    #Check the multiplication of two negative integers- positive scenario
    def test_multiply_method_2(self):
        result = calculator.multiply(-10, -3)
        self.assertEqual(result, 30)

    #Check the multiplication of one positive and one negative integer- positive scenario
    def test_multiply_method_3(self):
        result = calculator.multiply(10, -3)
        self.assertEqual(result, -30)

    #Check the multiplication of two integers- negative scenario
    def test_multiply_method_4(self):
        result = calculator.multiply(10, 3)
        self.assertNotEqual(result, 8)

    #Check the division of two positive  integers- positive scenario
    def test_divide_method_1(self):
        result = calculator.divide(30, 3)
        self.assertEqual(result, 10)

    #Check the division of two negative integers- positive scenario
    def test_divide_method_2(self):
        result = calculator.divide(-30, -3)
        self.assertEqual(result, 10)

    #Check the division of one positive and one negative integer- positive scenario
    def test_divide_method_3(self):
        result = calculator.divide(30, -3)
        self.assertEqual(result, -10)

    #Check the division of two integers- negative scenario
    def test_divide_method_4(self):
        result = calculator.divide(30, 3)
        self.assertNotEqual(result, 5)

    #Check the division of a number by 0/ this one doesn't work :(
    def test_divide_by_zero_method(self):
        result = calculator.divide(10, 0)
        self.assertRaises(ZeroDivisionError, result)

    #Check if result is rounded to 3 decimals
    ?

    #Check if user can exit calculator by typing “q”
    ?

    #Check if calculator says goodbye to an user
    ?