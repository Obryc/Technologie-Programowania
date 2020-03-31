"Napisz 3 przykłady własnych funkcji lambda"
import math

potegaN = lambda x , n: pow(x, n)
print(potegaN(3, 5))

silnaN = lambda n: math.factorial(n)
print(silnaN(231))


testIf = lambda n :print(1) if (n == 0) else print(n * math.factorial(n - 1))
print(testIf(4))