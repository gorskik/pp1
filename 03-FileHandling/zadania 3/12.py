with open('shoppinglist', 'a') as file:
    a=input('wprowadz nazwe prosuktu:')
    file.write(a+" ")
    
with open('shoppinglist', 'r') as file:
    print(file.read())