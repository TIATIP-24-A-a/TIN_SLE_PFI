import random
from functions.is_prime import is_prime


def generate_large_prime(bits=512):
    """Generiert eine große Primzahl mit einer angegebenen Bitlänge."""
    while True:
        num = random.getrandbits(bits) | 1  # Sicherstellen, dass die Zahl ungerade ist
        if is_prime(num):
            return num