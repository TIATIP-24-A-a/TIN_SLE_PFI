import unittest
from legacy.functions.generate_large_prime import generate_large_prime
from legacy.functions.is_prime import is_prime


class GenerateLargePrimeTests(unittest.TestCase):
    def test_generate_large_prime(self):
        result = generate_large_prime(512)
        number = is_prime(result)
        self.assertEqual(True, number)  # add assertion here

if __name__ == '__main__':
    unittest.main()
