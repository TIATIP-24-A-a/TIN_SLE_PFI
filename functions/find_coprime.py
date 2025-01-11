import random

from functions.greatest_common_divisor import greatest_common_divisor


def find_coprime(phi):
    """Findet eine Zahl e, die teilerfremd zu phi ist."""
    while True:
        e = random.randint(2, phi - 1)
        if greatest_common_divisor(e, phi) == 1:
            return e