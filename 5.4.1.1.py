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
