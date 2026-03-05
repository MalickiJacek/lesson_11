# Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
# stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
# klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
# przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
# pętli wydrukuj pole każdej figury.

class Figura():
    def oblicz_pole():
        pass

class Kwadrat(Figura):
    def __str__(self):
        return "Kwadrat"
    def __init__(self, bok: float):
        super().__init__()
        self.bok=bok
    def oblicz_pole(self):
        return(self.bok * self.bok)

class Kolo(Figura):
    def __str__(self):
        return "Koło"
    def __init__(self, r):
        super().__init__()
        self.r = r
    def oblicz_pole(self):
        return(self.r * self.r * 3.14159)

kwadrat = Kwadrat(10)
kolo = Kolo(5)

lista = [kolo, kwadrat]
for i in lista:
    print(f"pole {i}: {i.oblicz_pole()}")
