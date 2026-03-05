# Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
# metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y).

class Punkt():
    def __init__(self, x:float, y: float):
        self.x=x
        self.y=y
    def __str__(self):
        return(f"({self.x}; {self.y})")
    
point = Punkt(12324.1234, 123415.2342)

print(point)        