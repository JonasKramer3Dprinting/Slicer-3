def mit_zwei_multiplizieren(eingabe):
    eingabe = 2*eingabe
    print("Verdopple ich diese Zahl, so erhalte ich ",eingabe)


zahl = int(input("Gib eine ganze Zahl ein: "))
mit_zwei_multiplizieren(zahl)
zahl = int(input("Gib eine weitere ganze Zahl ein: "))
mit_zwei_multiplizieren(zahl)

print("Danke für die Eingabe.")



# Eingabe: Längen des Rechtecks
# Ausgabe in der Konsole: Fläche des Rechtecks
def flaeche_rechteck(a,b):
    print("Die Fläche des Rechtecks ist "+str(a*b)+".")

flaeche_rechteck(3,7)

flaeche_rechteck(2.3,5.1)

