moneta1=1
moneta2=2
moneta5=5
a=1
liczba=int(input("wprowadz kwote"))
liczbapokonwersji="posiadasz monety:"

if liczba/5>=1:
    while a==1:
        liczbapokonwersji=liczbapokonwersji + "moneta 5 "
        liczba=liczba-5
        if ((liczba/5)<1):
            a=0
a=1         
if liczba/2>=1:
    while a==1:
        liczbapokonwersji=liczbapokonwersji + "moneta 2 "
        liczba=liczba-2
        if ((liczba/2)<1):
            a=0
a=1       
if liczba/2>=1:
    while a==1:
        liczbapokonwersji=liczbapokonwersji + "moneta 1 "
        liczba=liczba-1
        if ((liczba/2)<1):
            a=0
            
print(liczbapokonwersji)
