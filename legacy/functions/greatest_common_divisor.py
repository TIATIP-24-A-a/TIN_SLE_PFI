def greatest_common_divisor(a, b):
    """Berechnet den grössten gemeinsamen Teiler (GCD) von a und b."""
    while b:
        a, b = b, a % b
    return a