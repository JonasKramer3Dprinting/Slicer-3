liste = []

while True:
    number = input("Zahl: ")
    if number == "":
        break
    else:
        liste.append(int(number))
    
liste.sort()

print(liste)