PIN="0805"

for i in range(3):
    PINwp=input("Wprowadź kod PIN: ")
    if PINwp==PIN:
        print("Kod prawidłowy")
        break
    elif PINwp!=PIN:
        print("Kod nie prawiłowy")
        if i==2:
            print("Karta płatnicza zablokowana")
        
