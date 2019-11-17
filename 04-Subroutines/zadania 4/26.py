def podatek(dochod):
    if dochod <= 5000 and dochod > 0:
        tax = dochod*17/100
        return tax
    elif dochod > 5000:
        tax = 5000*17/100 + (dochod-5000)*32/100
        return tax
    else: 
        return 'Zły dochód'

dochod = int(input('Podaj dochód: '))
print('Należny podatek:', podatek(dochod))