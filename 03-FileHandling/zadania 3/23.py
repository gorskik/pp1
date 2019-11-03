import re
sum = 0
with open('land.txt') as file:
    x = file.read()
    tab = re.findall('[0-9]', x)
    for cyfra in tab:
        sum += int(cyfra)
print(sum)
