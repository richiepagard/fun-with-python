"""
Test cases for Calculator class from calculator program.

Classes:
    TestCalculator: Test simple cases, special exceptions, and some special inputs
        of Calculator class methods.
"""

import unittest

from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Test class for Calculator class!

    Methods:
        setUp (self): Method for prepare the test fixture.
        test_simple_integer (self): Test calculator methods with simple integer inputs.
        test_simple_float (self): Test calculator methods with float numbers.
        test_simple_negative (self): Test calculator methods on negative numbers.
        test_zero_second_number (self): Test calculator methods with second number `0`.
    """

    def setUp(self):
        """
        Prepares the test fixtures.
        Create instances with different arguments for various scenarios.
        """
        self.simple_integer = Calculator(98, 7)
        self.simple_float = Calculator(4.87, 9.76)
        self.simple_negative = Calculator(-76, 45)

        self.zero_second_number = Calculator(67, 0)
        self.zero_numbers = Calculator(0, 0)

    def test_simple_integer(self):
        """
        Test simple integers on all calculator methods.
        """
        self.assertEqual(self.simple_integer.add(), 105)
        self.assertEqual(self.simple_integer.subtract(), 91)
        self.assertEqual(self.simple_integer.multiply(), 686)
        self.assertEqual(self.simple_integer.divide(), 14.0)

    def test_simple_float(self):
        """
        Test simple float inputs on all calculator methods.
        Use `assertAlmostEqual` instead of `assertEqual` for float comparisions
        to handle minor precision differences caused by floating-point representation.
        """
        self.assertAlmostEqual(self.simple_float.add(), 14.63, places=2)
        self.assertEqual(self.simple_float.subtract(), -4.89)
        self.assertAlmostEqual(self.simple_float.multiply(), 47.53, places=2)
        self.assertAlmostEqual(self.simple_float.divide(), 0.50, places=2)

    def test_simple_negative(self):
        """
        Test negative inputs on all calculator methods.
        """
        self.assertEqual(self.simple_negative.add(), -31)
        self.assertEqual(self.simple_negative.subtract(), -121)
        self.assertEqual(self.simple_negative.multiply(), -3420)
        self.assertEqual(self.simple_negative.divide(), -1.6888888888888889)

    def test_zero_second_number(self):
        """
        Test `0` for the second number on all calculator methods.
        Test `ZeroDivisionError` exception.
        """
        self.assertEqual(self.zero_second_number.add(), 67)
        self.assertEqual(self.zero_second_number.subtract(), 67)
        self.assertEqual(self.zero_second_number.multiply(), 0)

        with self.assertRaises(ZeroDivisionError):
            self.zero_second_number.divide()

    def test_zero_numbers(self):
        """
        Test `0` for both inputs on all calculator methods.
        """
        self.assertEqual(self.zero_numbers.add(), 0)
        self.assertEqual(self.zero_numbers.subtract(), 0)
        self.assertEqual(self.zero_numbers.multiply(), 0)

        with self.assertRaises(ZeroDivisionError):
            self.zero_numbers.divide()

    def test_type_error(self):
        """
        Test `type error` exception occured.    
        """
        with self.assertRaises(TypeError):
            Calculator(9, 'richie')

if __name__ == '__main__':
    unittest.main()
