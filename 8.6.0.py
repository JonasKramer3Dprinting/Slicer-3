class Fahrzeug:
    def __init__(self, marke, hubraum, leistung):
        self.marke = marke
        self.hubraum = hubraum
        self.leistung = leistung

    def get_infos(self):
        return "Marke: " + self.marke + ", Hubraum: " + \
    str(self.hubraum) + ", Leistung: " + str(self.leistung)

class Personenwagen(Fahrzeug):
    pass

class Lastwagen(Fahrzeug):
    pass

pw = Personenwagen("Opel", 222, 100)
lkw = Lastwagen("Mercedes", 5000, 300)
print(pw.get_infos())
print(lkw.get_infos())