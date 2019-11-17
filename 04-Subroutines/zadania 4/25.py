Imiona= ['Janek', 'Ania', 'Wojtek', 'Zosia', ]
imie=input('podaj imie:')
def jestImie(imie,imiona):
        if imie in imiona:
            print(f'Podane imie: {imie}')
            print(f'Imiona: {imiona}')
            print('Rezultat: Imie znajduje sie w wykazie.')    
        else:
            print(f'Podane imie: {imie}')
            print(f'Imiona: {imiona}')
            print('Rezultat: Imie nie znajduje sie w wykazie.')
            
jestImie(imie,Imiona)
        
        
