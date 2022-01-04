def teilermenge(n):
    liste = []
    for a in range(1, n + 1, 1):
        if n % a == 0:
            liste.append(a)
    print(liste)

teilermenge(int(input("Gib einen int: ")))