class Student():
    
    uczelnia = "UEK, Kraków"
    numer = 100000
    
    def __init__(self, imie, nazwisko, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr = Student.numer
        Student.numer+=1
        self.kierunek = kierunek
    
    def __str__(self):
        return f'''
        {self.imie} {self.nazwisko} ({self.numer}) {self.kierunek}
        '''
    
    
s1=Student('Krzysztof', 'Kowalski', 'IS')
s2=Student('Krzysztoff', 'Kowalski', 'IS')

print(s1,s2)