"""
Za pomocą dekoratora „wykonajXRazy” udekoruj 3 wybrane i napisane przez Ciebie funkcje (np.
funkcja mnożąca dwie liczby itp.). Sprawdź działanie udekorowanej funkcji

Spróbuj zmodyfikować dekorator, by dodawał od siebie napis „Wywolujemy dekorator”"""


def dekorator(oblicz):
    print("wywołujemy dekorator")
    def mOblicz(a,b):
        oblicz(a,b)
        oblicz(a,b)
        oblicz(a,b)
    return mOblicz

@dekorator
def oblicz(a,b):
    print(a/b)

x = range(1,100)
print(x)
oblicz(3,2)