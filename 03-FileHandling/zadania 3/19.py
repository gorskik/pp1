tab = []

with open('universities.txt', 'r') as file:
    for line in file:
        tab.append(line)

with open('universities.txt', 'w') as file:
    for i in sorted(tab):
        file.write(i)