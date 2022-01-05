# Neuer Bauplan für eine Person:
# Beim Erstellen eines Objekt der Klasse Person
# werden die Instanzvariablen direkt definiert.
class Person:
    def __init__(self, name, vorname, geb_datum, gewicht):
        self.name = name
        self.vorname = vorname
        self.geb_datum = geb_datum
        self.gewicht = gewicht
        self.set_gewicht(self.gewicht)
        while self.gewicht <= 0:
            self.set_gewicht(int(input("Gib Gewicht: ")))

    def set_gewicht(self, kubik):
        if (kubik <= 0):
            print("Error: Negativer Wert für das Gewicht! \
Der Wert wurde nicht geändert")
        else:
            self.gewicht = kubik
            print("Gewicht wurde geändert.")

    def get_gewicht(self):
        return self.gewicht

    def vorstellen(self):
        text = "Hallo.\nIch heisse " \
               + self.vorname + " " \
               + self.name + ", wiege " \
               + str(self.gewicht) + " kg und habe am " \
               + self.geb_datum + " Geburtstag.\n"\
               + "Nice to meet you."
        print(text)

    def abnehmen(self, wie_viel):
        print("Altes Gewicht:",self.gewicht,"kg")

        # Das neue Gewicht in der Instanzvariable
        # des Objektes speichern
        self.gewicht = self.gewicht - wie_viel

        print("Neues Gewicht:",self.gewicht,"kg")
    
paul = Person("Kramer", "Paul", "1999", -90)

