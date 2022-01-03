anzahl = int(input("Anzahl: "))
list = [0,1]
a = 0
while a < anzahl:
    list.append(list[a] + list[a + 1])
    print(list)
    a = a + 1