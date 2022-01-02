wertK = float(input("Engabe Wert k: "))
anzahlJahre = int(input("Anzahl Jahre: "))
abschreibungP = float(input("Abschreibung p: "))

zeitwertS = wertK
abschreibungsSteigung = 1 / (1 + 0.01 * abschreibungP)

jahre = 0
while jahre < anzahlJahre:
    jahre = jahre + 1
    zeitwertS = zeitwertS * abschreibungsSteigung
    print(zeitwertS)
    
print(wertK, zeitwertS)