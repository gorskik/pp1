a=int(input("wprowadz liczbe calkowita"))
b="twoja liczba w systemie binarnym to: "
if a==2:
    b=b+ '10'
else:
    reszta=a%2
    while reszta!=0:
        reszta=a%2
        if reszta==1:
            b=b+'1'
        else:
            b=b+ '0'

print(b)
    
    
    
    

