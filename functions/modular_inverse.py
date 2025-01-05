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