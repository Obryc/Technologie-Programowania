"Napisz generator funkcji silnia dla n podanego w argumencie"
import math
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * math.factorial(n - 1)

n = int(input("podaj liczbę n: "))
print(silnia(n))