# Einfachste Art eine Klasse zu erstellen
class Person:
    pass

p1 = Person()
print(p1)

e1 = Person()
e2 = Person()
e3 = Person()

print(e1)
print(e2)
print(e3)

p1.name = "Müller"
p1.vorname = "Kurt"
p1.geb_datum = "03.02.01"
p1.gewicht = 73.5

print(p1.name)
print(p1.vorname)