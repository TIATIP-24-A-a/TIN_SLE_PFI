import unittest
from functions.gcd import gcd


class GreatestCommonDivisorTest(unittest.TestCase):
    def test_gcd_of_(self):
        a = 6
        b = 9
        result = gcd(a, b)
        self.assertEqual(3, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
