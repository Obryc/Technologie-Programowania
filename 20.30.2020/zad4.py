"""Napisz program, który tworzy klasę Uczen o polach: i mię, nazwisko, liczba_pytan,
poprawne_odp. Napisać funkcję, która wczytuje dane, oraz funkcję, która oblicza procent
poprawnych odpowiedzi."""

class Uczen:
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.liczba_pytan = 40
        self.poprawne_odp = 0

    def wczytaj(self):
        self.imie = input("podaj imie" )
        self.nazwisko = input("podaj nazwisko" )
        self.liczba_pytan = input("podaj liczbe pytan" )
        self.poprawne_odp = input("podaj ilość poprawnych odp" )

    def oblicz(self):
        p = int(self.poprawne_odp)/int(self.liczba_pytan) * 100
        print(p, "%")

pr = Uczen()
pr.wczytaj()
pr.oblicz()