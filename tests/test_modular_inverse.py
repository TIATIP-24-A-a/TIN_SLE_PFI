import unittest
from functions.modular_inverse import modular_inverse


class ModularInverseTests(unittest.TestCase):
    def test_modular_inverse_(self):
        result = modular_inverse(7, 12)
        self.assertEqual(3, result)  # add assertion here

    def test_modular_inverse_8(self):
        result = modular_inverse(8,14)
        self.assertEqual(13, result)  # add assertion here

if __name__ == '__main__':
    unittest.main()
