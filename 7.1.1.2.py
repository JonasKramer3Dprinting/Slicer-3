def summe(n):
    summe = 0
    for a in range(1, n + 1, 1):
        summe = summe + a
    print(summe)

summe(int(input("Gib einen int: ")))