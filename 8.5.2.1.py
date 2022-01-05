class Motorrad():
    def __init__(self, marke, hubraum):
        self.marke = marke
        self.__hubraum = hubraum

    def set_hubraum(self, kubik):
        if (kubik <= 0):
            print("Error: Negativer Wert für den Hubraum! \
Der Wert wurde nicht geändert")
        else:
            self.__hubraum = kubik
            print("Hubraum wurde geändert.")

    def get_hubraum(self):
        return self.__hubraum

motrad = Motorrad("KTM", 950)
motrad.set_hubraum(600)
# motrad.__hubraum += 400
motrad.marke += ""
# print(motrad.__hubraum)
print(motrad.marke)
print(motrad.get_hubraum())