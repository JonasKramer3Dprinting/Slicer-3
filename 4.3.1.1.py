liste = ['Schwalbe', 'Kokosnuss', 13, 'Spam', 3,14]

print(liste[2])

print(len(liste))

liste.append('Ni')
print(liste)

liste.extend([4, 5, 3.14])
print(liste)

liste.insert(2,'Taube')
print(liste)

print(liste.count(3.14))

print(liste.index(3.14))

liste.remove(3.14)
print(liste)

liste.pop()
print(liste)