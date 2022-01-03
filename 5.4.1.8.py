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

for a in range(0, len(liste), 1):
    
    

    
    