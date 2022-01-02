from random import randint

zahl = 0
anzahlWürfe = 0

while not zahl == 6:
    zahl = randint(1,6)
    print(zahl)
    anzahlWürfe = anzahlWürfe + 1

print("Anzahl der Würfe: " + str(anzahlWürfe))
