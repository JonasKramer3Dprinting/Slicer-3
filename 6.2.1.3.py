jahr = int(input("Jahr: "))

if jahr % 400 == 0 or jahr % 4 == 0 and not jahr % 100 == 0:
    print("Das gegebene Jahr ist ein Schaltjahr.")
if not (jahr % 400 == 0 or jahr % 4 == 0 and not jahr % 100 == 0):
    print("Das gegebene Jahr ist kein Schaltjahr.")