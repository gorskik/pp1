import random

def rzut():
    a=random.randrange(1,7)
    return a
    
a='wyrzucone oczka: '
b=rzut()
c=rzut()
d=rzut()
a= ' '+a+str(b)+ ' '+str(c)+ ' '+str(d)+ ' '
suma=b+c+d
print(a)
print(f'suma oczek:  {suma}')
