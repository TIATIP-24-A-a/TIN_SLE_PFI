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