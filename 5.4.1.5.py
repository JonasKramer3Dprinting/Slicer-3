zahl = int(input("Zahl: "))
while not zahl == 1:
    print(zahl)
    if zahl % 2 == 1:
        zahl = 3 * zahl + 1
    else: 
        zahl = int(0.5 * zahl)
print(zahl)