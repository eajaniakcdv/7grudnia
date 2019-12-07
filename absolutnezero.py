from liczba import Number
#import liczba - to wtedy jest w kontenerze jakby czyli liczba.number a nie samo number.
class AbsolutZero(Number):
    #pass
    def __init__(self):
        self.value = 0

    def __str__(self):
        return("jestes zerem")

    def reklama(self):
        print("ucz sie!")

zero = AbsolutZero()
print(zero)
print ("Zaimportowano modul", __name__)
