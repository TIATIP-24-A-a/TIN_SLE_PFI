import unittest
from legacy.functions.greatest_common_divisor import greatest_common_divisor


class GreatestCommonDivisorTests(unittest.TestCase):
    def test_greatest_common_divisor_of_6_9(self):
        a = 6
        b = 9
        result = greatest_common_divisor(a, b)
        self.assertEqual(3, result)  # add assertion here

    def test_greatest_common_divisor_of_2_9(self):
        a = 2
        b = 9
        result = greatest_common_divisor(a, b)
        self.assertEqual(1, result)  # add assertion here

if __name__ == '__main__':
    unittest.main()
