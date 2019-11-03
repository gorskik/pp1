numbers = []
with open('numbers.txt', 'r') as file:
    for line in file:
        if int(line)%2==0:
            numbers.append(line)
        
with open('evennumbers', 'w') as file:
    for i in numbers:
        file.write(i)
        

    