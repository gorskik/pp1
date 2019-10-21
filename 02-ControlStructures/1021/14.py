wiek = input("podaj wiek psa ")
wiek = float(wiek)
if (wiek < 3):
    ludzkie = wiek * 10.5
elif (wiek > 2):
    ludzkie = 2*10.5+4*(wiek-2)

print(ludzkie)