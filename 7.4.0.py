g = lambda x: x**2
print(g(2) * g(3))


def temp_funktion(x):
    return x + 42

def make_list(f,groesse):
    ergebnis = []
    for i in range(groesse):
        ergebnis.append(f(i))
    return ergebnis

a = make_list(temp_funktion, 5)
print(a)

[42, 43, 44, 45, 46]

def make_list(f,groesse):
    ergebnis = []
    for i in range(groesse):
        ergebnis.append(f(i))
    return ergebnis

a = make_list(lambda x: x + 42, 5)
print(a)

[42, 43, 44, 45, 46]