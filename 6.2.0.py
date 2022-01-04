var_1 = int(input("Gib Zahl: "))
var_2 = int(input("Gib Zahl: "))

if var_1 > var_2 or var_1 == var_2:
    print("Die erste Zahl ist größer gleich der zweiten Zahl.")
if var_1 < var_2 or var_1 == var_2:
    print("Die erste Zahl ist kleiner gleich der zweiten Zahl.")
if var_1 < var_2 or var_1 > var_2:
    print("Die erste Zahl ist ungleich der zweiten Zahl.")

if not var_1 == var_2:
    print("Die erste Zahl ist ungleich der zweiten Zahl.")

if var_1 == 10 and var_1 > var_2:
    print("Die erste Zahl hat den Wert 10 und ist größer als die zweite Zahl.")