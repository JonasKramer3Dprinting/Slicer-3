anzahlZahlen = int(input("Bis zu welcher Zahl sollen die Primzahlen reichen: "))
listePrimzahlen = []

for zähler1 in range(2, anzahlZahlen + 1, 1):
    teiler = 0
    for zähler2 in range(2, zähler1, 1):
        if zähler1 % zähler2 == 0:
            teiler = teiler + 1
    if teiler == 0:
        listePrimzahlen.append(zähler1)

print(listePrimzahlen)
