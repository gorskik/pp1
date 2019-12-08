class Telewizory():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def on(self):
        self.is_on= True
    def off(self):
        self.is_on = False
    def show_status(self):
        print(f'Telewizor jest włączony, kanał - {self.channel_no}' if self.is_on == True else 'telewizor jest wyłączony')
        
tv1=Telewizory()
tv1.show_status()
tv1.on()
tv1.show_status()