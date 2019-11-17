tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def suma(tab):
    c=0
    x=0
    while x<len(tab):
        if isinstance(tab[x],int):
            c+=tab[x]
            x+=1
        else:
            c+=suma(tab[x])
            x+=1
    return c            
print(suma(tab))