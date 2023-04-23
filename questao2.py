# Utilizando o código da questão anterior para dar
# exemplo de herança múltipla. Podem ser criadas
# as classes ElectricVehicle, ElectricBus e ElectricCar
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        bus_fare = super().fare()
        return bus_fare * 1.1


# Classe ElectricVehicle com informação de electric_range
class ElectricVehicle:
    def __init__(self, electric_range):
        self.electric_range = electric_range


# Classes ElectricBus e ElectricCar
# Tem-se o electric_range e o electric_fare
# Ao fare total adiciona-se o electric_fare
class ElectricBus(Bus, ElectricVehicle):
    def __init__(self, name, mileage, capacity, electric_range):
        Bus.__init__(self, name, mileage, capacity)
        ElectricVehicle.__init__(self, electric_range)

    def fare(self):
        bus_fare = super().fare()
        electric_fare = self.electric_range * 20
        return bus_fare + electric_fare


class ElectricCar(Vehicle, ElectricVehicle):
    def __init__(self, name, mileage, capacity, electric_range):
        Vehicle.__init__(self, name, mileage, capacity)
        ElectricVehicle.__init__(self, electric_range)

    def fare(self):
        car_fare = super().fare()
        electric_fare = self.electric_range * 10
        return car_fare + electric_fare


# Exemplo de aplicação 1
elbus = ElectricBus("Bus 1", 10, 50, 20)
print("Electric Bus fare is:", elbus.fare())
# Saída: Electric Bus fare is: 5900.0

# Exemplo de aplicação 2
elcar = ElectricCar("Car 1", 10, 50, 20)
print("Electric Car fare is:", elcar.fare())
# Saída: Electric Car fare is: 5200

print(ElectricBus.__mro__)
# Saída:(<class '__main__.ElectricBus'>, <class '__main__.Bus'>,
# <class '__main__.Vehicle'>, <class '__main__.ElectricVehicle'>,
# <class 'object'>)


print(ElectricCar.__mro__)
# Saída: (<class '__main__.ElectricCar'>, <class '__main__.Vehicle'>,
# <class '__main__.ElectricVehicle'>, <class 'object'>)
