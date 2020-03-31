". Napisz generator ciągu arytmetycznego o różnicy 2 do n podanego w argumencie"
n = int(input("podaj zakres: "))

def coDwa(n):
    for n in range(n+1):
        if n % 2 == 0:
            continue
        print(n)

coDwa(n)
