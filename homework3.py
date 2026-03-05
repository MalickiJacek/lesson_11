# Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
# oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
# dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
# stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje.

class Worker():
    def __init__(self, name, paid_per_hour:float):
        self.name=name
        self.paid_per_hour = paid_per_hour

    def count_payment(self, hours:int):
        return(self.paid_per_hour*hours)
    
class Programist(Worker):
    def __init__(self, name, paid_per_hour, languages):
        super().__init__(name, paid_per_hour)
        self.languages=languages

dev = Programist("Jan", 100, "react")
print(dev.count_payment(168))
    
