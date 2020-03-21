#Stworzyć klasy:
#- Trójkąt
#- Prostokąt
#- Koło
#- Romb
#- Trapez
#- Dla każdej z tych klas stworzyć odpowiednie pola, a także stworzyć metody ustawiające
#zmienne, a także obliczające pola powierzchni i obwody tych figur.
#- Przetestować działanie klas poprzez utworzenie obiektów i wywołanie metod
import math

class Trojkat:
    def __init__(self):
        self.a = name = input("podaj a: ")
        self.b = name = input("podaj b: ")
        self.c = name = input("podaj c: ")

        print("Obwód wynosi:", (int(self.a) + int(self.b) + int(self.c)))
        p = 0.5 * (int(self.a) + int(self.b) + int(self.c))  # obliczmy współczynnik wzoru Herona
        P = math.sqrt(p * (p - int(self.a)) * (p - int(self.b)) * (p - int(self.c)))
        print("Pole wynosi:", P)


class Prostokat:
    def __init__(self):
        self.a = name = input("podaj a: ")
        self.b = name = input("podaj b: ")


        print("Obwód wynosi:", (int(self.a) * 4))
        p = int(self.a) * int(self.b)
        print("Pole wynosi:", p)

class Kolo:
    def __init__(self):
        self.r = name = input("podaj r: ")
        self.Pi = name = input("podaj Pi: ")

        print("Obwód wynosi:", (int(self.r) * 2 * int(self.Pi)))
        p = float(self.Pi) * math.sqrt(int(self.r))
        print("Pole wynosi:", p)

class Romb:
    def __init__(self):
            self.a = name = input("podaj a: ")
            self.b = name = input("podaj b: ")
            self.c = name = input("podaj c: ")
            self.d = name = input("podaj d: ")
            self.h = name = input("podaj h: ")

            print("Obwód wynosi:", (int(self.a) + int(self.b) + int(self.c) + int(self.d)))
            p = float(self.a) * 4
            print("Pole wynosi:", p)

class Trapez:
    def __init__(self):
        self.a = name = input("podaj a:")
        self.b = name = input("podaj b: ")
        self.c = name = input("podaj c: ")
        self.d = name = input("podaj d: ")
        self.h = name = input("podaj h: ")

        print("Obwód wynosi:", (int(self.a) + int(self.b) + int(self.c) + int(self.d) ))
        p = (float(self.a) + self.b)/2 * float(self.h)
        print("Pole wynosi:", p)

x = input("podaj figure: ")
if x== "Trapez":
    Trapez()
elif x=="romb":
    Romb()
elif x == "Kolo":
    Kolo()
elif x == "prostokat":
    Prostokat()
else:
    Trojkat()