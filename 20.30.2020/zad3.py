"""Napisz program, który oblicza wysokość podatku dochodowego dla podanej podstawy
obliczenia podatku. Podatek wynosił będzie 18 % z podstawy dochodu minus kwota
zmniejszająca podatek 556 zł 02 gr (klasa Podatnik o polach: imie, nazwisko,
podstawa_podatku)."""

class Podatnik:
    def __init__(self):
        self.kwota = input("podaj kwote do podatkowania: ")
        self.imie = input("podaj imie: ")
        self.nazwisko = input("podaj nazwisko: ")

        p = 0.18 * (float(self.kwota) - 556.02)
        print("kwota wynosi", p)

Podatnik()