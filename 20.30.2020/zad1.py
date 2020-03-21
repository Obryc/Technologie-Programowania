class Pojazd:
    def __init__(self):
        self.nazwa = ""
        self.rodzaj = "auto"
        self.kolor = ""
        self.wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." %(self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu
    


Auto1=Pojazd()
Auto1.nazwa="ferrari"
Auto1.kolor="czerwony"
Auto1.rodzaj="kabriolet"
Auto1.wartosc=60000

Auto2=Pojazd()
Auto2.nazwa="Ikarus"
Auto2.kolor="niebieski"
Auto2.rodzaj="autobus"
Auto2.wartosc=10000

print (Auto1.opis())
print (Auto2.opis())