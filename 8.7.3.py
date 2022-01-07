class Brüche():
    def __init__(self, zähler, nenner):
        self.zähler = zähler
        self.nenner = nenner
        self.set_nenner(self.nenner)
        while self.nenner == 0:
            self.set_nenner(int(input("Gib Nenner: ")))

    def set_nenner(self, nenner):
        if nenner == 0:
            print("Error: Ungültiger Wert für den Nenner! \
            Der Wert wurde nicht geändert")
        else:
            self.nenner = nenner
            print("Wert wurde geändert.")

    def print_wert(self):
        print("Der Wert des Bruches beträgt " + str(self.zähler) + "/" + str(self.nenner) + ".")
    
    def add(self, objekt):
        zähler = self.zähler * objekt.nenner  + objekt.zähler * self.nenner
        nenner = self.nenner * objekt.nenner

        self.kürzen()

        return (Brüche(zähler, nenner))

    def multiply(self, objekt):
        zähler = self.zähler * objekt.zähler
        nenner = self.nenner * objekt.nenner

        self.kürzen()

        return (Brüche(zähler, nenner))

    def kürzen(self):
        self.print_wert()

        anzahlPrimzahlen = 1000
        zähler = 0
        zähler2 = 0
        teiler = 0
        listePrimzahlen = []

        while anzahlPrimzahlen > zähler:
            zähler = zähler + 1
            zähler2 = 0
            teiler = 0
            while zähler > zähler2:
                zähler2 = zähler2 + 1
                if zähler % zähler2 == 0:
                    teiler = teiler + 1
            if teiler == 2: 
                listePrimzahlen.append(zähler2)
        
        zahl1 = self.zähler
        zahl2 = self.nenner

        listeGemeinsameTeiler = []

        länge = len(listePrimzahlen)
        zähler1 = 0
        while länge > zähler1:
            while True:
                if zahl1 % listePrimzahlen[zähler1] == 0 and zahl2 % listePrimzahlen[zähler1] == 0:
                    listeGemeinsameTeiler.append(listePrimzahlen[zähler1])
                else:
                    break
                zahl1 = zahl1 / listePrimzahlen[zähler1]
                zahl2 = zahl2 / listePrimzahlen[zähler1]
            zähler1 = zähler1 + 1

        print(listeGemeinsameTeiler)

        teiler = 1
        for a in range (0, len(listeGemeinsameTeiler), 1):
            teiler = teiler * listeGemeinsameTeiler[a]
        
        self.zähler = int(self.zähler / teiler)
        self.nenner = int(self.nenner / teiler)

        self.print_wert()

    def equal(self, objekt):
        wahrheit = False
        if self.zähler / self.nenner == objekt.zähler / objekt.nenner:
            wahrheit = True
        return wahrheit


bruch = Brüche(16, 8)
bruch.print_wert()

bruch2 = Brüche(5, 1)

bruch3 = bruch.add(bruch2)
bruch3.print_wert()

bruch4 = bruch.multiply(bruch2)
bruch4.print_wert()

bruch = Brüche(800, 600)
bruch.kürzen()

print(bruch.equal(bruch))

