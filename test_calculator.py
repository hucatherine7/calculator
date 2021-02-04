#Tests

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(0, 0), 0)
        self.assertEqual(calculator.addition(99, 11), 110)
        self.assertEqual(calculator.addition(-9, -5), -14)
        self.assertEqual(calculator.addition(1.2, -1.3), -0.10000000000000009)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(0, 0), 0)
        self.assertEqual(calculator.subtraction(14, 5), 9)
        self.assertEqual(calculator.subtraction(-8, -7), -1)
        self.assertEqual(calculator.subtraction(4.9, 1.2), 3.7)

    def test_division(self):
        self.assertEqual(calculator.division(3, 0), "undefined")
        self.assertEqual(calculator.division(3, 2), 1.5)
        self.assertEqual(calculator.division(48, 12), 4)
        self.assertEqual(calculator.division(-20, 5), -4)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(0, 0), 0)
        self.assertEqual(calculator.multiplication(14, 4), 56)
        self.assertEqual(calculator.multiplication(-4, -3), 12)
        self.assertEqual(calculator.multiplication(0.5, 100), 50)


if __name__ == '__main__':
    unittest.main(verbosity=2)
