import unittest

from functions.get_private_key import get_private_key

class ModularPowerTests(unittest.TestCase):
    def test_modular_inverse_of_1(self):
        p = 223  # die Primzahlen p und q
        q = 127
        e = 121
        phi = (p - 1) * (q - 1)
        result = get_private_key(e, phi)
        self.assertEqual(5317, result)  # add assertion here

    def test_modular_inverse_of_15(self):
        p = 223  # die Primzahlen p und q
        q = 127
        e = 235
        phi = (p - 1) * (q - 1)
        result = get_private_key(e, phi)
        self.assertEqual(7975, result)  # add assertion here

if __name__ == '__main__':
    unittest.main()
