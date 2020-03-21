"""Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c. Klasa powinna
zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze. Główną metodą powinna być
Rozwiaz(), która zwraca miejsca zerowe podanej funkcji. Należy zwrócić uwagę na przypadki gdy
a=0, b=0 lub c=0, a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub
zerze rozwiązań."""
from math import sqrt

class FunkcjaKwadratowa:
    def __init__(self):
        print("funkcja kwadratowa : (a * x^2) + b*x + c")
        self.a = float(input("a: "))
        self.b = float(input("b: "))
        self.c = float(input("c: "))

        self.r = self.b ** 2 - 4 * self.a * self.c

    def Rozwiaz(self):
        if r > 0:

            x1 = (((-float(self.b) + sqrt(self.r)) / (2 * self.a)))
            x2 = (((-float(self.b) - sqrt(self.r)) / (2 * self.a)))
            print("dwa miejsca zerowe: %f and %f" % (x1, x2))
        elif r == 0:

            x = (-float(self.b) / 2 * self.a)
            print("jedno miejsce zerowe: ", x)
        else:

            print("brak miejsc zerowych < 0.")
            exit()

pr = FunkcjaKwadratowa()
pr.Rozwiaz()