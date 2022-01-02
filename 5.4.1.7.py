liste = []
listeG = []

while True:
    wort = input("Wort: ")
    if wort == "":
        break
    else:
        if wort == wort.capitalize():
            listeG.append(True)
            liste.append(wort.lower())
        else:
            listeG.append(False)
            liste.append(wort)

liste.sort()
for a in range(0, len(liste), 1):
    if listeG[a] == True:
        lokal = str(liste[a])
        liste[a] = lokal.capitalize()

print(liste)