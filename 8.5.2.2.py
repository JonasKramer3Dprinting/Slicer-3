class Motorrad():
    def __init__(self, marke, hubraum):
        self.marke = marke
        self.__hubraum = hubraum
        self.set_hubraum(self.__hubraum)
        while self.__hubraum <= 0:
            self.set_hubraum(int(input("Gib Hubraum: ")))

    def set_hubraum(self, kubik):
        if (kubik <= 0):
            print("Error: Negativer Wert für den Hubraum! \
Der Wert wurde nicht geändert")
        else:
            self.__hubraum = kubik
            print("Hubraum wurde geändert.")

    def get_hubraum(self):
        return self.__hubraum

das_rad = Motorrad("Buell", -1200)
