# Berechnet aus dem öffentlichen Schlüssel e den privaten Schlüssel (das multiplikative Inverse von e modulo phi)
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