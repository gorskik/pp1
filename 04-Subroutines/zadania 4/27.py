tekst='Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
def ile(a,tekst):
    suma=0
    for x in tekst:
        if x==a: suma+=1
    return suma
a=input('Podaj samogłoskę: ')
print(f'Samogłoska {a} występuje w tekście {ile(a,tekst)} razy.')