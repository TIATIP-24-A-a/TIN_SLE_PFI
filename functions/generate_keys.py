from functions.find_coprime import find_coprime
from functions.generate_large_prime import generate_large_prime
from functions.modular_inverse import modular_inverse


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