from random import randint

satz = input("Gib Satz: ")

wörter = 0
großbuchstaben = 0

if not satz == "":
    wörter = 1

for zeichen in satz:
    if zeichen == " ":
        wörter = wörter + 1
    if zeichen == zeichen.capitalize() and not zeichen == " ":
        großbuchstaben = großbuchstaben + 1
    
print("Anzahl Wörter: " + str(wörter))
print("Anzahl Großbuchstaben: " + str(großbuchstaben))

wörterListe = [satz[0]]

for a in range(1, len(satz), 1):
    if not satz[a] == " ":
        wörterListe[len(wörterListe) - 1] = wörterListe[len(wörterListe) - 1] + satz[a]
    else:
        wörterListe.append("")

listeWörter = wörterListe
liste = []
for a in range(0, len(listeWörter), 1):
    liste.append([])
    for b in range(1, len(listeWörter[a]) - 1, 1):
        liste[a].append(listeWörter[a][b])

print(listeWörter)
print(liste)
listeÜberarbeitet = []

for a in range(0, len(liste), 1):
    listeZufallszahlen = []
    listeKopie = []
    for b in range(0, len(liste[a]), 1):
        listeZufallszahlen.append(b)
        listeKopie.append(liste[a][b])
    print(listeZufallszahlen)
    lokal2 = []
    for b in range(0, len(liste[a]), 1):
        lokal = randint(0, len(listeZufallszahlen) - 1)
        print(lokal)
        lokal2.append(listeKopie[lokal])
        listeZufallszahlen.remove(listeZufallszahlen[lokal])
        listeKopie.remove(listeKopie[lokal])
        print(listeZufallszahlen)
        print(lokal2)
    listeÜberarbeitet.append(lokal2)

print(liste)
print(listeÜberarbeitet)
print(listeWörter)

listeNeueWörter = []
for a in range(0, len(listeWörter), 1):
    wort = listeWörter[a][0]
    for b in range(0, len(liste[a]), 1):
        wort = wort + listeÜberarbeitet[a][b]
    wort = wort + listeWörter[a][-1]
    print(wort)
    listeNeueWörter.append(wort)

print(listeWörter)
print(listeNeueWörter)