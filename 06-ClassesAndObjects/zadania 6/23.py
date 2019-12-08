class Kontakt:
    def __init__(self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon
        
class Lista_kontaktow:
    def __init__(self):
        self.kontakty = []
        
    def add(self, kontakt):
        self.kontakty.append(kontakt)
        
    def show(self):
        for x in self.kontakty:
            print(f'{x.nazwa}'+' '*(16-len(x.nazwa))+f'{x.email}'+' '*(16-len(x.email))+f'{x.telefon}')
k1= Kontakt('aniaw', 'aniagorsa@gmail.com', '444455433223')
k2= Kontakt('aniaq', 'aniagorfa@gmail.com', '444232333223')    
k3= Kontakt('aniae', 'aniagorda@gmail.com', '444345543223')

lista=Lista_kontaktow()
lista.add(k1)
lista.add(k2)
lista.add(k3)

lista.show()

    