# Para o polimorfismo, utiliza-se o contexto de figuras geométricas
# São criadas as classes abstratas abaixo
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Para o Duck Typing, utiliza-se o contexto de transportes
# São criadas as classes
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def move(self):
        return "The car is moving on the road"


class Bicycle(Transport):
    def move(self):
        return "The bicycle is moving on the street"


class Boat(Transport):
    def move(self):
        return "The boat is moving on the water"


# Demonstração: Polimorfismo
# Para todas as subclasses, o método area pode ser
# utilizado polimorficamente
# Exemplo de aplicação
circle = Circle(6)
square = Square(5)
rectangle = Rectangle(3, 11)

for shape in (circle, square, rectangle):
    print(shape.area())
# Saída:
# 113.04
# 25
# 33


# Demonstração: Duck Typing
# Pode ser definida uma função para chamar o método move
def move_vehicle(vehicle):
    print(vehicle.move())


# Exemplo de aplicação:
car1 = Car()
bicycle1 = Bicycle()
boat1 = Boat()

# Exemplificando o Duck Typing
for vehicle in (car1, bicycle1, boat1):
    move_vehicle(vehicle)
# Saída:
# The car is moving on the road
# The bicycle is moving on the street
# The boat is moving on the water
