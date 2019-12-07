class Number:
    # def __new__(self):
    #     print("Metoda new")
    def __init__(self,wartosc):
        print("Metoda init wywolana")
        self.value = wartosc

    def wyzeruj(self):
        self.value = 0

    def ustaw(self, ustaw):
        self.value = ustaw

numer = Number(2)
#numer2 = Number()
numer.wyzeruj()
print(numer.value)
print (numer.value)
print ("OOOO!!! Wykonalo sie")
print ("Zaimportowano modul", __name__)
