# Neuer Bauplan für eine Person:
# Beim Erstellen eines Objekt der Klasse Person
# werden die Instanzvariablen direkt definiert.
class Person:
    def __init__(self, name, vorname, geb_datum, gewicht):
        self.name = name
        self.vorname = vorname
        self.geb_datum = geb_datum
        self.gewicht = gewicht

paul = Person("Kramer", "Paul", "1999", 90)
print(paul.name, paul.vorname, paul.geb_datum, paul.gewicht)

p2 = Person("Smith", "John", "04.04.04", 83)
print(p2.name, p2.vorname, p2.geb_datum, p2.gewicht)