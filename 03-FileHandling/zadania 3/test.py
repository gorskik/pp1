import re

sum = 0
with open('land.txt') as file:
    x = file.read()
    tab = re.findall('[0-9]', x)
    for i in tab:
        sum += int(i)

print(sum)