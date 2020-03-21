class Student:
    pass

class Pracownik:
    message = "do roboty"

class osoba(Student, Pracownik):

    def __init__(self, who):

        self.name = who

I1 = osoba("Adam")
I2 = osoba("Bogdan")

print ( I1.name )
print ( I1.message )
print ( I2.message )
print ( Pracownik.message )

print ( osoba.__bases__ )