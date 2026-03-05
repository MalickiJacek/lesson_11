# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
# obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii

class Product():
    def __init__(self, name: str, price: float, category:str):
        self.name=name
        self.price = price
        self.category = category
bike = Product("bike", 100, "vehicle")

print(bike.name)
print(bike.price)
print(bike.category)