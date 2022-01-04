print(len("Haus"))

# Eingabe: Längen des Rechtecks
# Ausgabe in der Konsole: Fläche des Rechtecks
def flaeche_rechteck(a, b):
    print("Die Fläche des Rechtecks ist " + str(a * b) + ".")

def flaeche_rechteck_return(a, b):
    return a * b

print(flaeche_rechteck_return(2, 5))