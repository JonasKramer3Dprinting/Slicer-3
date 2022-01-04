def fakultaet(zahl):
    zahl1 = 1
    for a in range(2, zahl + 1, 1):
        zahl1 = zahl1 * a
    return zahl1

print(fakultaet(3))

print(fakultaet(5))