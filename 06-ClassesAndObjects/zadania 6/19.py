class Bank_account:
    def __init__(self,no):
        self.no = no
        self.balance = 0
        
    def incom(self, incom):
        self.balance+= incom
        
    def pay(self, pay):
        self.balance-= pay
        
    def status(self):
        print(f'Numer rachunku: {self.no}\nSaldo: {self.balance} zł')
        
my_a = Bank_account("12 3456 5555 9090 1111 0000 7722")
my_a.status()
my_a.incom(25.30)
my_a.status()
my_a.pay(31.70)
my_a.status()
my_a.pay(14)
my_a.status()
    
        