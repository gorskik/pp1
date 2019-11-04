tab=[4,3,7,1,3]
suma=0

def suma(tablica):
    suma=0
    for element in tablica:
        suma=element+suma
    return suma
print('tablica:', *tab, sep=" ")
print('Suma wartości:{suma(tab)}')
    