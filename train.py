class Animal:
    description="Some kind of Animal"
    def __init__(self, name, age):
        self.name = name
        self.__age=age
    def __str__(self):
        return(f"u tried to print me!, I'm {self.name}")
    def __add__(self, other):
        return self.__age + other.__age
    def say_hello(self):
        return "Hello"
    def introduce_yourself(self):
        return(f"my name is {self.name}")
    def zmien_imie(self, name: str):
        self.name=name
    def show_age(self):
        return(f"my age is {self.__age}")
dog = Animal("Azor", 10)

cat = Animal("Mruczek", 15)

print(dog.name)
print(cat.name)

print(dog.description)
print(cat.description)

print(dog.say_hello())
#teoretycznie można tak zmienić, ale polecane jest używanie do tego metod
dog.name = "Burek"
dog.zmien_imie("Burekk")
print(dog.name)
print(dog._Animal__age) #dojście do ukrytego
print(dog.show_age())

snake = Animal("waz", 10)
print(snake) #działa dzięki __str__
print(snake + cat) #działa dzięki metodzie __add__
print(isinstance(dog, Animal))
