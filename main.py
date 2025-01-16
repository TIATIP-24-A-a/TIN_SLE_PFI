from functions.get_private_key import get_private_key
from functions.rsa import rsa

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