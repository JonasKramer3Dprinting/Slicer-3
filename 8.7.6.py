class Person:
    def __init__(self, name, male, alter):
        self.name = name
        self.male = male
        self.__alter = alter

    def get_beschreibung(self):
        return "Ich heisse " + self.name + ", bin " + self.male  + ", " + str(self.__alter) + " Jahre alt und " + self.get_class() + "."

    def get_class(self):
        if isinstance(self, Pensionierter):
            return "Pensionör(in)"
        elif isinstance(self, Kind):
            return "Kind"
        else: 
            return "Erwachsene(r)"

    def set_alter(self, alter):
        self.__alter = alter

    def get_alter(self):
        return self.__alter



class Pensionierter(Person):
    def __init__(self, name, male, alter, rente): 
        super().__init__(name, male, alter)
        self.__rente = rente

    def set_rente(self, rente):
        self.__rente = rente

    def get_rente(self):
        return self.__rente



class Kind(Person):
    def __init__(self, name, male, alter, anzahl_zähne, spielzeug): 
        super().__init__(name, male, alter)
        self.__anzahl_zähne = anzahl_zähne
        self.spielzeug = spielzeug
    
    def set_anzahl_zähnae(self, anzahl_zähne):
        self.__anzahl_zähne = anzahl_zähne

    def get_rente(self):
        return self.__anzahl_zähne

    def spielzeug_tauschen(self):
        print(self.spielzeug)
        self.spielzeug = input("Neues Spielzeug")



class Erwachsener(Person):
    def __init__(self, name, male, alter, lohn, ist_verheiratet, kinder): 
        super().__init__(name, male, alter)
        self.__lohn = lohn
        self.ist_verheiratet = ist_verheiratet
        self.kinder = kinder

    def set_lohn(self, lohn):
        self.__lohn = lohn

    def get_lohn(self):
        return self.__lohn

    def print_kinder(self):
        print(self.kinder)



pen = Pensionierter("Paul Kramer", "männlich", 24, 1000)
print(pen.get_beschreibung())

kid = Kind("Paul Kramer", "männlich", 24, 32, "LEGO")
print(kid.get_beschreibung())

adult = Erwachsener("Paul Kramer", "männlich", 24, 5000, True, 3)
print(adult.get_beschreibung())

print(0.7 / 28)

print(pen.get_alter())

pen.set_alter(25)

print(pen.get_alter())

print(pen.get_rente())

pen.set_rente(2000)

print(pen.get_rente())
