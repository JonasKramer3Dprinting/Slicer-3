lieferwagenPreisProKilometer = 1.6
lastwagenPreisProKilometer= 2.8

lieferwagenStrecke = 85
lastwagenStrecke = 120

lieferwagenPreis = lieferwagenPreisProKilometer * lieferwagenStrecke
lastwagenPreis = lastwagenPreisProKilometer * lastwagenStrecke

print("Lieferwagenpreis: " + str(lieferwagenPreis))
print("Lastwagenpreis: " + str(lastwagenPreis))