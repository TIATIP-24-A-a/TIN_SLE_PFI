# TIN_SLE_PFI_rsa

# Project RSA
We chose RSA encryption algorithm for this project. We defined the following requirements:

- Clear structure of the RSA-relevant functions
- Encryption of plain text
- Decryption of encrypted text

# Creation of Algorithm

### 07.12.2024 Create Main RSA Functions

For our next project we chose the RSA encryption algorithm.
In our first step, we did research to understand what RSA means and how it works.
We created a test repository as our playground and tested several functions.

For our first code we used this template below.

````python

p = 13
q = 17
n = p * q
phi = (p - 1) * (q - 1)

# Schl�sselgenerierung
e = 11
d = inverse(e, phi)
print("�ffentlicher Schl�ssel: ({:d},{:d})".format(e, n))
print("Privater Schl�ssel: ({:d},{:d})".format(d, n))

````

At the beginning, we created the function `generate_keys` to generate the key pair and used the default bit length (`bit=512`) for the generated the keys. 
We tried to figure how this function works and this is what we learned:
With `p` and `q` the two large prime numbers are generated and the value `n` is calculated by `n = p * q`.
Phi is generated by the formula `ϕ=(p−1)⋅(q−1)` and is necessary to determine the value `e` which must coprime with `ϕ`.
After `e` was determined the value `d` is calculated with as a modular inverse from `e module ϕ`.


````python
def generate_keys(bits=512):
    """Generiert ein Schlüsselpaar für RSA."""
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = find_coprime(phi)  # Öffentlicher Exponent
    d = modular_inverse(e, phi)  # Privater Exponent

    return (e, n), (d, n)

if __name__ == "__main__":
    # Beispiel: Generiere RSA-Schlüssel
    public_key, private_key = generate_keys(bits=512)
    print("Öffentlicher Schlüssel:", public_key)
    print("Privater Schlüssel:", private_key)

````


### 14.12.2024 Create Functions

For generating a large prime number we used the function `generate_large_prime`. It generates a random number and ensures to be an odd number if `| 1` is used.
After the large prime number is generated, `ìs_prime` checks if it is really a prime number. As soon as a valid primer number is found the function (`return`) returns it.


````python
def generate_large_prime(bits=512):
    """Generiert eine große Primzahl mit einer angegebenen Bitlänge."""
    while True:
        num = random.getrandbits(bits) | 1  # Sicherstellen, dass die Zahl ungerade ist
        if is_prime(num):
            return num

````
````python
def is_prime(n, k=5):
    """Prüft, ob eine Zahl n eine Primzahl ist (Miller-Rabin-Test)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

````

### 21.12.2024 Create Functions

We added the modular inverse function for our `d = modular_inverse(e, phi)`variable. This formula is calculated with the following formula: `(e⋅d) mod ϕ = 1`.


````python
def modular_inverse(e, phi):
    """Berechnet das multiplikative Inverse von e modulo phi."""
    old_r, r = phi, e
    old_s, s = 1, 0
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    if old_s < 0:
        old_s += phi
    return old_s
````

For the `e = find_coprime(phi)` variable we added the `find_coprime` function.
The parameter `phi` is a positive number that is looking for a number `e` which is coprime to phi.
For `random.randint(2, phi - 1)` a random number is generated in the range of `2` and `phi-1`.
If the greatest common (`GCD`) divisor is equal to `1` the function returns. Otherwise another number is chosen until a valid number is found.

````python
def find_coprime(phi):
    """Findet eine Zahl e, die teilerfremd zu phi ist."""
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e
````


### 11. - 17.01.2025

It appeared that the codes we created are too complicated for us to explain. As well we were not able to prove whether the code worked properly or not and if the numbers are correct.
Therefore, we created a new code which is easier to understand and to explain.

As a result, for our new code we decided to not generate prime numbers and only generate the private key. The rest is most likely the same in theory and our public key is defined by `e = 121 `. 


For the unittests we used the usual TDD procedure.

````Python
def main():
    p = 223  # die Primzahlen p und q
    q = 127
    n = p * q
    e = 121  # Der öffentliche Schlüssel
    phi = (p - 1) * (q - 1)
    d = get_private_key(e, phi)  # Erzeugt den privaten Schlüssel

    klartext = "Mache die Projektarbeit fertig"
    text = [ord(c) for c in klartext]  # Umwandlung des Klartexts in eine Liste von ASCII-Werten

    rsa(text, n, e)  # Verschlüsseln
    # Ausgabe des verschlüsselten Texts auf der Konsole:
    print('Verschlüsselter Text:')
    print(' '.join(map(str, text)))

    rsa(text, n, d)  # Entschlüsseln
    # Ausgabe des Dechiffrats:
    print('Entschlüsselter Text:')
    print(''.join(map(chr, text)))

if __name__ == "__main__":
    main()
````

````Python
def get_private_key(e, phi):
    a = phi
    b = e
    d = 0
    u = 1
    while b != 0:
        q = a // b
        x = b  # Variable zum Zwischenspeichern
        b = a - q * b
        a = x
        x = u
        u = d - q * u
        d = x
    if a > 1:
        print("Fehler: e und phi nicht teilerfremd")
        exit(1)
    return d
````

````Python
# Diese Funktion berechnet die Potenz a ^ b modulo n
def modular_power(a, b, n):
    res = a if b & 1 else 1
    b >>= 1
    while b:
        a = (a * a) % n
        if b & 1:
            res = (res * a) % n
        b >>= 1
    return res
````

````Python
from functions.modular_power import modular_power
# Diese Funktion ver- oder entschlüsselt den Klartext 'text' elementweise mit dem Schlüssel 'key'
def rsa(text, n, key):
    for i in range(len(text)):  # for-Schleife, die die Zeichen des Textes durchläuft
        text[i] = modular_power(text[i], key, n)  # ver- bzw. entschlüsselt text[i]
````
### Unittests

````Python
from main import main
# Benchmark the RSA encryption and decryption process using pytest-benchmark
def test_rsa_benchmark(benchmark):
    result = benchmark(main)
    assert result == None
````
````Python
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
````
````Python
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
````
````Python
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
````

## Sources
All work was evaluated and implemented with the help of the articles mentioned below

### Flowchart
- Mermaid.js - https://mermaid.js.org/intro/getting-started.html

### RSA
- RSA MIT Paper - https://people.csail.mit.edu/rivest/Rsapaper.pdf
- RSA tutorial - https://studyflix.de/informatik/rsa-verschlusselung-1608

### Benchmark and Diagram
- matplotlib - https://matplotlib.org/stable/users/index
- pytest-benchmark - https://pytest-benchmark.readthedocs.io/en/latest/
- Big O Complexity - https://web.mit.edu/16.070/www/lecture/big_o.pdf

### Python
- Hello World - https://www.learnpython.org/en/Hello%2C_World!
- Variables and Types - https://www.learnpython.org/en/Variables_and_Types
- Lists - https://www.learnpython.org/en/Lists
- Basic Operators - https://www.learnpython.org/en/Basic_Operators
- Conditions - https://www.learnpython.org/en/Conditions
- Loops - https://www.learnpython.org/en/Loops
- Functions - https://www.learnpython.org/en/Functions

### Git
- Git - https://git-scm.com/docs
- Commits - https://www.conventionalcommits.org/en/v1.0.0/
- Git Actions https://docs.github.com/en/actions

### Markdown
- Md doc - https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
