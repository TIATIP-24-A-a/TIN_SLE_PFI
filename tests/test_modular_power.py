import unittest

from functions.modular_power import modular_power

class ModularPowerTests(unittest.TestCase):
    def test_modular_inverse_of_1(self):
        e = 121
        n = 223 * 127
        result = modular_power(1, e, n)
        self.assertEqual(1, result)  # add assertion here

    def test_modular_inverse_of_15(self):
        e = 121
        n = 223 * 127
        result = modular_power(15, e, n)
        self.assertEqual(8506, result)  # add assertion here

if __name__ == '__main__':
    unittest.main()
