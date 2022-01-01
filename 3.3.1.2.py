breite = float(input("Gib Breite: "))
länge = float(input("Gib Länge: "))
höhe = float(input("Gib Höhe: "))

xy = (breite**2 + länge**2)**0.5
xz = (breite**2 + höhe**2)**0.5
yz = (länge**2 + höhe**2)**0.5
xyz = (breite**2 + länge**2 + höhe**2)**0.5

print("Diagonale xy: " + str(xy))
print("Diagonale xz: " + str(xz))
print("Diagonale yz: " + str(yz))
print("Raumdiagonale xyz: " + str(xyz))