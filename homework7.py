# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
# (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
# metody do zarządzania telewizorem:
# wlacz() i wylacz()
# zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
# jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
# nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
# 100. 

class Tv():
    def __init__(self, channel:int=1, volume:int=10, turned_on:bool=False):
        self.__channel=channel
        self.__volume=volume
        self.__turned_on = turned_on

    def wlacz(self):
        self.__turned_on=True

    def wylacz(self):
        self.__turned_on=False

    def change_channel(self, channel: int):
        if self.__turned_on:
            self.__channel=channel
            return(f"Channel changed to: {channel}")
        else:
            return(f"Cannot change channel while Tv is off...")
        
    def up_volume(self):
        if self.__turned_on:
            if self.__volume == 100:
                return "Volume reached 100 already"
            else:
                self.__volume+=1
                return(f"Volume changed to: {self.__volume}")
        else:
            return(f"Cannot change volume while Tv is off...")
    def down_volume(self):
        if self.__turned_on:
            if self.__volume == 0:
                return "Volume reached 0 already"
            else:
                self.__volume-=1
                return(f"Volume changed to: {self.__volume}")
        else:
            return(f"Cannot change volume while Tv is off...")

    def set_volume(self, value):
        if self.__turned_on:
            if value <=100 and  value >=0:
                return(f"Volume changed to: {value}")
            else: 
                return("U typed in wrong volume to be set. Must be from 0 to 100")


        else:
            return(f"Cannot change volume while Tv is off...")
    def info(self):
        return(f"Turned on? {self.__turned_on}, Channel: {self.__channel}, Volume: {self.__volume}")
    
my_tv = Tv(15, 100, True)
my_tv1 = Tv()

print(my_tv1.change_channel(10))
my_tv1.wlacz()
print(my_tv1.change_channel(14))
print(my_tv.up_volume())
print(my_tv.set_volume(150))