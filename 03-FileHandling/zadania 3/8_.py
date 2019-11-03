with open('DanePersonalne.txt','w') as file:
    file.write('Krzysztof Górski\n Uek \n IS')
with open('DanePersonalne.txt','r') as file:
    print(file.read())
    