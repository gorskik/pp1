class TV():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = []
        self.volume = 0
        
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel(self,new_channel_no):
        self.channel = new_channel_no
    def show_status(self,tab):
        if self.is_on == True:
            print(f'Telewizor jest włączony. Numer kanału: {self.channel} {tab[self.channel-1]} Głośność:{self.volume}')
            
        else:
            print('Telewizor jest wyłączony.')
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print('LISTA KANAŁÓW TV')
        for x in range(len(self.channels)):
            print(f'{x+1}. {self.channels[x]}')
    def increase_vol(self):
        if self.volume<10:
            self.volume+=1
    def decrease_vol(self):
        if self.volume>0:

            self.volume-=1

tab=['TVP1','TVP2','TVN','POLSAT','TVN7','ABC','TVNTurbo']


tv1 = TV()
tv1.on()
tv1.show_status(tab)
tv1.increase_vol()
tv1.show_status(tab)
