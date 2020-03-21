"""Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c. Klasa powinna
zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze. Główną metodą powinna być
Rozwiaz(), która zwraca miejsca zerowe podanej funkcji. Należy zwrócić uwagę na przypadki gdy
a=0, b=0 lub c=0, a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub
zerze rozwiązań."""

import math

class FunkcjaKwadratowa:
    def __init__(self):
        self.a = input("podaj a: ")
        self.b = input("podaj b: ")
        self.c = input("podaj c: ")

    def rozwiaz(self):
        self.r = int(self.b) ** 2 - 4 * int(self.a) * int(self.c)
        if self.r > 0:
            x1 = (((-int(self.b)) + math.sqrt(int(self.r))) / (2 * int(self.a)))
            x2 = (((-int(self.b)) - math.sqrt(int(self.r))) / (2 * int(self.a)))
            print("dwa miejsca zerowe: %f i %f" % (x1, x2))
        elif self.r == 0:
            x = (-int(self.b)) / 2 * int(self.a)
            print("jedno miejsce zerowe: ", x)
        else:
            print("brak miejsc zerowych")
            exit()

pr = FunkcjaKwadratowa()
pr.rozwiaz()