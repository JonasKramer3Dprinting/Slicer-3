from random import randrange

summe = 0
augenzahl = 0
anzahlWürfe = 0

while summe < 100:
    augenzahl = randrange(1,6)
    anzahlWürfe = anzahlWürfe + 1
    summe = summe + augenzahl

print(anzahlWürfe, summe)



summe = 0
augenzahl = 0
anzahlWürfe = 0
liste = [0,0,0,0,0,0]

while summe < 100:
    augenzahl = randrange(1,7)
    anzahlWürfe = anzahlWürfe + 1
    summe = summe + augenzahl
    liste[augenzahl - 1] = liste[augenzahl - 1] + 1

print(anzahlWürfe, summe)
print(liste)



summe = 0
augenzahl = 0
anzahlWürfe = 0
liste = [0,0,0,0,0,0]
wahrheit = False

while wahrheit == False:
    augenzahl = randrange(1,7)
    anzahlWürfe = anzahlWürfe + 1
    summe = summe + augenzahl
    liste[augenzahl - 1] = liste[augenzahl - 1] + 1
    zähler = 0
    while zähler < 5:
        zähler = zähler + 1
        if liste[zähler] == 50:
            wahrheit = True
            

print(anzahlWürfe, summe)
print(liste)