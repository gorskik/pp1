import random

class Kostka():
    def __init__(self):
        self.liczba_oczek = 0
    
    def throw(self):
        self.liczba_oczek = random.randrange(1, 7)
        


k1=Kostka()
k2=Kostka()
k3=Kostka()
suma=0
for x in range (0,3):
    k1.throw()
    print(f'rzut koscia 1 :{k1.liczba_oczek}')
    k2.throw()
    print(f'rzut koscia 2 :{k2.liczba_oczek}')
    k3.throw()
    print(f'rzut koscia 3 :{k3.liczba_oczek}')
    suma+=k1.liczba_oczek+k2.liczba_oczek+k3.liczba_oczek
    
print(f'suma oczek wyrzuconych to:{suma}')

    