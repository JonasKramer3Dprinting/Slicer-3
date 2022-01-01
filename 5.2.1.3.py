jahr = int(input("Jahr: "))
if jahr % 400 == 0:
    print("Das gegebene Jahr ist ein Schaltjahr.")
else:
    if jahr % 4 == 0 and not jahr % 100 == 0:
        print("Das gegebene Jahr ist ein Schaltjahr.")
    else:
        print("Das gegebene Jahr ist kein Schaltjahr.")