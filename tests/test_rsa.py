import unittest

from functions.rsa import rsa
from functions.get_private_key import get_private_key


class RsaTests(unittest.TestCase):
    def test_rsa_encrypt(self):
        p = 223  # die Primzahlen p und q
        q = 127
        n = p * q
        e = 121  # Der öffentliche Schlüssel
        text = "Mache die Projektarbeit fertig"
        ascii_text = [ord(c) for c in text]
        rsa(ascii_text, n, e)
        match = "19012 20586 7850 25415 7881 10422 14249 6663 7881 10422 12639 8479 23366 11586 7881 234 26526 20586 8479 13217 7881 6663 26526 10422 27105 7881 8479 26526 6663 3735"
        result =' '.join(map(str, ascii_text))
        self.assertEqual(result, match)

    def test_rsa_decrypt(self):
        q = 127
        p = 223
        e = 121  # Der öffentliche Schlüssel
        n = p * q
        phi = (p - 1) * (q - 1)
        d = get_private_key(e, phi)  # Erzeugt den privaten Schlüssel
        text = "Mache die Projektarbeit fertig"
        ascii_text = [ord(c) for c in text]
        rsa(ascii_text, n, e)
        rsa(ascii_text, n, d)
        self.assertEqual(text, text)

if __name__ == '__main__':
    unittest.main()
