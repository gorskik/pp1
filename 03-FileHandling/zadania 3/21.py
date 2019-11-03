suma = 0
liczby = 0
with open('numbersinrows.txt') as file:
    for line in file:
        split = line.split(',')
        liczby += len(split)
        for i in split:
            suma += int(i)
print(f'Ilość liczb w pliku: {nums}. Ich suma: {sum}')