import random
a = False

while (a==False):
    rzut_komputera = random.randrange(1,7)
    guess = int(input("podaj ile wyrzucil komputer"))
    
    if (rzut_komputera == guess):
        print("true")
        a = True
        
        
    else:
        print("false")

    


