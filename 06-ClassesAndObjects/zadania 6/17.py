class Ulamek:
    def __init__(self,licznik,mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        
    def show(self):
        print(f'{self.licznik}/{self.mianownik}')
        
    def easier(self):
        dzielnik=0
        for x in range(0,self.licznik-1):
            if self.licznik % (self.licznik-x)==0 and self.mianownik % (self.licznik-x)==0:
                dzielnik = self.licznik-x
                self.licznik //= dzielnik
                self.mianownik //= dzielnik
                
u1 = Ulamek(25,30)
u1.show()
u1.easier()
u1.show()
