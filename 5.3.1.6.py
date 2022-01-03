jahresbetrag = float(input("Jahresbetrag: "))
zins = float(input("Zins: "))
zielbetrag = float(input("Zielbetrag: "))

steigung = 1 + 0.01 * zins
betrag = 0
jahre = 0
while betrag < zielbetrag:
    jahre = jahre + 1
    betrag = (betrag + jahresbetrag) * steigung
    print("Jahr: " + str(jahre) + ", Betrag: " + str(betrag))