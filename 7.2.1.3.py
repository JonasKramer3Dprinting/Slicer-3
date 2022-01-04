def meine_funktion(a,b):
    while b != 0:
        t = a%b
        a = b
        b = t
    return a

print(meine_funktion(12,16))
print(meine_funktion(1,16))
print(meine_funktion(8,16))
print(meine_funktion(8,21))
print(meine_funktion(18,21))
print(meine_funktion(27,36))