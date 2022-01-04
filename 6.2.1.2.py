zahl = int(input("Gib eine Zahl ein: "))
   
if zahl % 2 == 0 and zahl % 3 == 0:
    print("Die eingegebene Zahl ist durch drei und zwei teilbar.")
if zahl % 2 == 0 and not zahl % 3 == 0: 
    print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")
if not zahl % 2 == 0:
    print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")