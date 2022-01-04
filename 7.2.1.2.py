def quersumme(zahl):
    größe = 0
    quersumme = 0
    liste = []
    zahl_kopie = zahl
    zahl_kopie_kopie = zahl_kopie
    while zahl_kopie >= 10:
        größe = größe + 1
        zahl_kopie = zahl_kopie / 10
    größe_kopie = größe
    for a in range (0, größe + 1, 1):
        liste.append(zahl_kopie_kopie // (10 ** größe_kopie))
        print(liste)
        zahl_kopie_kopie = zahl_kopie_kopie - liste[a] * (10 ** größe_kopie)
        größe_kopie = größe_kopie - 1
    for a in range(0, len(liste), 1):
        quersumme = quersumme + liste[a]
    return quersumme
    
print(quersumme(100045))
    

