# tests/test_math_tools.py
import unittest
from my_awesome_lib.math_tools import factorial, gcd

class TestMathTools(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_gcd(self):
        self.assertEqual(gcd(48, 180), 12)
        self.assertEqual(gcd(101, 10), 1)

if __name__ == '__main__':
    unittest.main()
 
