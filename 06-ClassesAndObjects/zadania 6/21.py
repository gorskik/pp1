class Statystyka():
    def __init__(self):
        self.tab = []
        
    def add(self):
        self.tab.append(int(input('podaj liczbe do dodania')))
    def show_split(self):
        for x in self.tab:
            print (x, end = ' , ')
    def najwieksza(self):
        return max(self.tab)
    def najmniejsza(self):
        return min(self.tab)
    def srednia(self):
        return sum(self.tab)/len(self.tab)
    def mediana(self):
        import statistics
        return statistics.median(self.tab)
    def show(self):
        print(f'Najmniejsza liczba: {self.najmniejsza()}\nNajwiększa liczba: {self.najwieksza()}\nŚrednia arytmetyczna: {self.srednia()}\nMediana: {self.mediana()}')
liczby = Statystyka()
for x in range(5):
    liczby.add()
liczby.show()


        
        
liczby= Statystyka()       
for x in range (0,5):
    liczby.add()
liczby.show_split()
    

        