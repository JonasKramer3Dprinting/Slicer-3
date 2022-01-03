immobilie = float(input("Wert der Immobilie: "))
p = float(input("Wert der jährlichen Steigung: "))
immobilieNeu = immobilie
anzahl = 0
while not immobilieNeu > immobilie * 2:
    anzahl = anzahl + 1
    immobilieNeu = immobilieNeu * (1 + 0.01 * p)
    print(anzahl, immobilieNeu)