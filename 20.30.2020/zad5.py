"""Stworzyć klasę książka. Dodać autora, ilość stron i wydawnictwo, rok wydania. Stworzyć jako pole
spis rozdziałów (tablica char). Dodać metody ustawiające."""

class Ksiazka:
    def __init__(self):
        self.autor = ""
        self.ilosc_stron = 0
        self.wydawnictwo = ""
        self.rok_wydania = 0
        self.rozdzialy = []
    def dodaj(self):
        self.autor = input("podaj autora: ")
        self.ilosc_stron= input("ilosc_stron: ")
        self.wydawnictwo = input("wydawnictwo: ")
        self.rok_wydania = input("rok wydania: ")
        while True:
            x = input("podaj nazwe rozdzialu")
            self.rozdzialy.append(x)
            print(self.rozdzialy)
            w = input("czy kontynuować? Y/N")
            if w == "Y":
                continue
            else:
                break

pe = Ksiazka()
pe.dodaj()