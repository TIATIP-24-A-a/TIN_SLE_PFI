# RSA in python
Von Sheryl Leutenegger, Pedro Figueiredo, Tim Ineichen

# Einleitung
Dieses Dokument beschreibt den Ablauf und unsere Umsetzung des Projekts "RSA in python".

# Anforderungen
- Klarer Aufbau der RSA relevanten Funktionen
- Verschlüsselung von Klartext
- Entschlüsselung von verschlüsseltem Text

# Funktionalität
## 1. Initialisierung
- Zwei Primzahlen `p = 223` und `q = 127` werden gewählt. Der Modulus `n` wird als Produkt von `p` und `q` berechnet:  
  `n = p * q`

## 2. Schlüsselerzeugung
- Der öffentliche Exponent `e = 121` wird gewählt.
- Die Eulersche Totientfunktion `φ(n)` wird berechnet:  
  `φ(n) = (p - 1) * (q - 1)`
- Der private Schlüssel `d` wird mit der Funktion `get_private_key` berechnet, sodass `d * e ≡ 1 (mod φ(n))`.

## 3. Textverschlüsselung
- Der Klartext („Mache die Projektarbeit fertig“) wird in ASCII-Werte umgewandelt.
- Die `rsa`-Funktion verschlüsselt den Text mit dem öffentlichen Schlüssel `(e, n)`.

## 4. Ausgabe des verschlüsselten Textes
- Der verschlüsselte Text wird als eine durch Leerzeichen getrennte Zahlenreihe ausgegeben.

## 5. Entschlüsselung
- Die `rsa`-Funktion wird erneut aufgerufen, um den verschlüsselten Text mit dem privaten Schlüssel `(d, n)` zu entschlüsseln.
- Der entschlüsselte Text wird zurück in Zeichen umgewandelt und ausgegeben.

## Beispieloutput
- Der verschlüsselte Text wird ausgegeben, gefolgt von dem entschlüsselten Text, der der ursprünglichen Nachricht entspricht.


# Fazit
- Es gibt diverse Möglichkeiten ein Problem zu Lösen
- RSA war evtl. ein zu komplizertes Thema für unsere Gruppenzusammenstellung
- Manchmal braucht es mehrere Anläufe
