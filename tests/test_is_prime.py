import unittest
from functions.is_prime import is_prime


class IsPrimeTests(unittest.TestCase):
    def test_is_prime_of_7(self):
        result = is_prime(7)
        self.assertEqual(True, result)  # add assertion here

    def test_is_prime_of_8(self):
        result = is_prime(8)
        self.assertEqual(False, result)  # add assertion here

if __name__ == '__main__':
    unittest.main()
