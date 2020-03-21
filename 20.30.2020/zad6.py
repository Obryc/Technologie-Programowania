"""Napisz klasę odcinek w przestrzeni dwuwymiarowej (x,y). Klasa ta ma zawierać:
Punkt początkowy i punkt końcowy.
Metodę zwracającą długość odcinka"""

import math
class odcinek:
    def __init__(self):
        self.x1 = input ("podaj x1")
        self.y1 = input ("podaj y1")
        self.x2 = input ("podaj x2")
        self.y2 = input ("podaj y2")


    def dystans(self):
        dist = math.sqrt((int(self.x2) - int(self.x1)) ** 2 + (int(self.y2) - int(self.y1)) ** 2)
        print(dist)

pr = odcinek()
pr.dystans()