# Zadanie 1 – Klasa Film
# Zadania z gwiazdką (challenge)
# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
# rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
# informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
# obiekty tej klasy i wydrukuj informacje o nich.

class Film():
    def __init__(self, title, director, year):
        self.title=title
        self.director=director
        self.year=year

    def information(self):
        return(f'"{self.title}"({self.year}), directed by: {self.director}')
    
interstellar = Film("Interstellar", "Nolan", 2014)
        
print(interstellar.information())


