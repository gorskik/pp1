numbers = []
with open('numbers.txt') as file:
    for line in file:
        numbers.append(int(line))
        
numbers.sort()

for i in numbers:
    print(i, end = " ")