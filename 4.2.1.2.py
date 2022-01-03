eingabe = str(input("Gib einen Text ein: "))

zwischenspeicher = eingabe[0]
zwischenspeicher = zwischenspeicher.capitalize()
zwischenspeicher_2 = ""
for a in range(1,len(eingabe),1):
    zwischenspeicher_2 = zwischenspeicher_2 + eingabe[a]
eingabe = zwischenspeicher + zwischenspeicher_2
eingabe = eingabe + "!"

print(eingabe)


