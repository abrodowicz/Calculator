import calculator
import unittest
from unittest.mock import Mock, patch

class TestCalculator(unittest.TestCase):

    #Check if calculator greet an user
    def test_greeting_display(self):
        self.assertEqual(calculator.welcome(), "Hello! This is your calculator.")

    #Check if calculator provide an instruction
    def test_instruction_display(self):
        self.assertEqual(calculator.instruction(), """
This calculator works on two numbers.
You can perform actions from list below:
Adding-> +
Subtracting-> -
Multiplying-> *
Dividing-> /
To quit the program enter 'q'
Let's start!
    """)

    #Check operator validation- positive scenario
    def test_operator_validation_1(self):
        operator = calculator.getOperator("/")
        self.assertEqual(operator, "/")

    #Check operator validation- negative scenario
    def test_operator_validation_2(self):
        operator = calculator.getOperator("m")
        self.assertEqual(operator, None)

    #Check input validation- positive scenarios: a) decimal number
    def test_inputs_validation_1(self):
        result = calculator.add(1.2, 3.4)
        self.assertEqual(result, 4.6)

    #Check input validation- positive scenarios: c) input with space
    @patch("calculator.input")
    @patch("calculator.print")
    def test_inputs_validation_2(self, mock_print, mock_input):
        mock_input.side_effect = ['1. 5', '+', '1. 4', 'no']
        with self.assertRaises(SystemExit):
            calculator.calculate()
        mock_print.assert_called_with('Goodbye!')

    #Check input validation- positive scenarios: d) input with coma
    @patch("calculator.input")
    @patch("calculator.print")
    def test_inputs_validation_3(self, mock_print, mock_input):
        mock_input.side_effect = ['1,5', '+', '1,5', 'no']
        with self.assertRaises(SystemExit):
            calculator.calculate()
        mock_print.assert_called_with('Goodbye!')

    #Check input validation- negative scenario
    def test_inputs_validation_4(self):
        with self.assertRaises(TypeError):
            calculator.add("m", 2)

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
        self.assertEqual("The divisor must not be zero", result)

    #Check if result is rounded to 3 decimals
    def test_rounding_result_method(self):
        result = calculator.divide(1, 3)
        self.assertEqual(result, 0.333)

    #Check if user can exit calculator by typing “q” instead of proper operator
    def test_exit_by_q_instead_of_operator(self):
        with self.assertRaises(SystemExit):
            calculator.getOperator('q')

    #Check if user can exit calculator by typing “q” instead of proper first number input
    @patch("calculator.input")
    @patch("calculator.print")
    def test_exit_by_q_instead_of_first_number(self, mock_print, mock_input):
        mock_input.side_effect = ['q', '+', '4', 'no']
        with self.assertRaises(SystemExit):
            calculator.calculate()
        mock_print.assert_called_with('You quit calculator!')

    #Check if user can exit calculator by typing “q” instead of proper second number input
    @patch("calculator.input")
    @patch("calculator.print")
    def test_exit_by_q_instead_of_second_number(self, mock_print, mock_input):
        mock_input.side_effect = ['1', '+', 'q', 'no']
        with self.assertRaises(SystemExit):
            calculator.calculate()
        mock_print.assert_called_with('You quit calculator!')

    #Check if calculator says goodbye to an user
    @patch("calculator.input")
    @patch("calculator.print")
    def test_goodbye_2(self, mock_print, mock_input):
        mock_input.side_effect = ['5', '+', '4', 'no']
        with self.assertRaises(SystemExit):
            calculator.calculate()
        mock_print.assert_called_with('Goodbye!')