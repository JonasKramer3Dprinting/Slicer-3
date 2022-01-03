from random import randint

zahl = randint(1,6)

gerateneZahl = 0
anzahlVersuche = 0

while not gerateneZahl == zahl:
    gerateneZahl = gerateneZahl + 1
    anzahlVersuche = anzahlVersuche + 1

print(anzahlVersuche)