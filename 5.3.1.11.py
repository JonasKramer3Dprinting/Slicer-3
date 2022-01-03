anzahlPrimzahlen = 1000
zähler = 0
zähler2 = 0
teiler = 0
wahrheit = False
listePrimzahlen = []

while anzahlPrimzahlen > zähler:
    zähler = zähler + 1
    zähler2 = 0
    teiler = 0
    while zähler > zähler2:
        zähler2 = zähler2 + 1
        if zähler % zähler2 == 0:
            teiler = teiler + 1
    if teiler == 2: 
        listePrimzahlen.append(zähler2)
    
print(listePrimzahlen)

zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))

listeGemeinsameTeiler = []

länge = len(listePrimzahlen)
zähler1 = 0
while länge > zähler1:
    while True:
        if zahl1 % listePrimzahlen[zähler1] == 0 and zahl2 % listePrimzahlen[zähler1] == 0:
            listeGemeinsameTeiler.append(listePrimzahlen[zähler1])
        else:
            break
        zahl1 = zahl1 / listePrimzahlen[zähler1]
        zahl2 = zahl2 / listePrimzahlen[zähler1]
    zähler1 = zähler1 + 1

print(listeGemeinsameTeiler)