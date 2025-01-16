import unittest

from legacy.functions.find_coprime import find_coprime


class FindCoprimeTests(unittest.TestCase):
    def test_find_coprime_of_12(self):
        phi = 12
        result = find_coprime(phi)
        is_result_in_range = 2 <= result <= phi - 1
        self.assertEqual(is_result_in_range, True)

    def test_find_coprime_of_3(self):
        phi = 3
        result = find_coprime(phi)
        is_result_in_range = 2 <= result <= phi - 1
        self.assertEqual(is_result_in_range, True)

if __name__ == '__main__':
    unittest.main()
