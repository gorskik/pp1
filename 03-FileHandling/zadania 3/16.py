import re
x = 0
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}', komunikat)
print(cyfry)
for i in cyfry:
    x += int(i)
print(f'Średnia temperatura: {x/3}')