from functions.modular_power import modular_power
# Diese Funktion ver- oder entschlüsselt den Klartext 'text' elementweise mit dem Schlüssel 'key'
def rsa(text, n, key):
    for i in range(len(text)):  # for-Schleife, die die Zeichen des Textes durchläuft
        text[i] = modular_power(text[i], key, n)  # ver- bzw. entschlüsselt text[i]