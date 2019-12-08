class Telewizory():
    def __init__(self):
        self.is_on = False
    def on(self):
        self.is_on= True
    def off(self):
        self.is_on = False
    def show_status(self):
        print('Telewizor jest włączony' if self.is_on == True else 'telewizor jest wyłączony')
        
tv1=Telewizory()
tv1.show_status()
tv1.on()
tv1.show_status()