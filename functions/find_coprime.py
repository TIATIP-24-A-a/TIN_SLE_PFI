def find_coprime(phi):
    """Findet eine Zahl e, die teilerfremd zu phi ist."""
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e