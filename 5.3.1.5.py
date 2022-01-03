einkaufspreis = int(input("Einkaufspreis: "))
jahre = int(input("Jahre: "))
linear = einkaufspreis / jahre
a = 0
while a < jahre:
    a = a + 1
    einkaufspreis = einkaufspreis - linear
    print("Jahr " + str(a) + ": " + str(einkaufspreis))
 
    