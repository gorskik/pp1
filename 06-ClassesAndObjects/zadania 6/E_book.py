class E_book:
    def __init__(self, tytul, autor, strony):
        self.tytul = tytul
        self.autor=autor
        self.strony=strony
        self.b_strona = 0
        self.otwarta = False
        
    def open(self):
        self.otwarta = True
    def show_status(self):
        if self.otwarta==True:
            print(f' Tytuł: {self.tytul} Autor: {self.autor} l.stron: {self.strony} aktualna storna: {self.b_strona}')
        else:
            print(f' Tytuł: {self.tytul} Autor: {self.autor} l.stron: {self.strony} aktualna storna: ksiazka jest zamknieta')
    def przeczytaj_strone(self):
        if self.otwarta == True:
            self.b_strona += 1
        else:
            print('ksiazka jest zamknieta')
            

            
            
        