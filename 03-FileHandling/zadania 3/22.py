with open('students.txt', 'r') as file:
    for line in file:
        s=line.split(',')
        if s[2]!='age':
            if int(s[2])<30:
                print(f'{s[0]} {s[1]} {s[3]} {s[4]}') #no nie wiem co tu by wymyslec
