wzrost = float(input("podaj wzrost"))
waga = float(input("podaj wage"))
BMI = ((waga)/(wzrost**2))*10000
print (f"twoje BMI to: {BMI}")

if BMI < 18.5:
    print("Niedowaga")
elif BMI > 18.5 and BMI < 24.9:
    print("Waga prawidłowa")
elif BMI > 24.9 and BMI < 30:
    print("Nadwaga")
elif BMI >= 30:
    print("Otyłość")

