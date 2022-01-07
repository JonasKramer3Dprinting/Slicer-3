class Mitarbeiter():
    def __init__(self, vornahme, nachname, lohn):
        self.vorname = vornahme
        self.nachname = nachname
        self.lohn = lohn
        self.set_vorname(self.vorname)
        while self.vorname == "":
            self.set_vorname(input("Gib Vorname: "))
        self.set_nachname(self.nachname)
        while self.nachname == "":
            self.set_nachname(input("Gib Nachname: "))
        self.set_lohn(self.lohn)
        while self.lohn <= 3800:
            self.set_lohn(int(input("Gib Lohn: ")))

    def set_vorname(self, name):
        if name == "":
            print("Error: Ungültiger Wert für den Vornamen! \
            Der Wert wurde nicht geändert")
        else:
            self.vorname = name
            print("Wert wurde geändert.")

    def set_nachname(self, name):
        if name == "":
            print("Error: Ungültiger Wert für den Nachnamen! \
            Der Wert wurde nicht geändert")
        else:
            self.nachname = name
            print("Wert wurde geändert.")

    def set_lohn(self, lohn):
        if lohn <= 3800:
            print("Error: Ungültiger Wert für den Lohn! \
            Der Wert wurde nicht geändert")
        else:
            self.lohn = lohn
            print("Wert wurde geändert.")
    
    def get_mitarbeiter_id(self):
        print("Ich heisse " + self.vorname + " " + self.nachname + " (alias " + self.get_initialen() + "). Mein Lohn bei dieser Firma beträgt " + str(self.lohn) + " sfr.")
    
    def lohn_erhöhen(self, erhöhung):
        self.lohn = self.lohn + erhöhung

    def lohn_senken(self, senkung):
        if self.lohn - senkung > 3800:
            self.lohn = self.lohn - senkung
            print("Erfolg: Der Lohn wurde um " + str(senkung) + " sfr. gesenkt und beträgt nun " + str(self.lohn) + " sfr.")
        else:
            print("Error: Der Lohn kann wegen der Mindestlohninitative nicht gesenkt werden.")
            print("Er bleibt bei " + str(self.lohn) + " sfr.")
            print("Bitte mit der Gewerkschaft reden.")

    def get_initialen(self):
        initialen = self.vorname[0] + "." + self.nachname[0] + "."
        return initialen

jonas = Mitarbeiter("Jonas", "Kramer", 4200)
jonas.get_mitarbeiter_id()
print(jonas.lohn)
jonas.lohn_erhöhen(800)
print(jonas.lohn)
jonas.lohn_senken(1000)
jonas.lohn_senken(1000)
print(jonas.get_initialen())