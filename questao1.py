# A classe Bus é completada de modo que a sua fare tenha
# um adicional de 10% em cima do fare do vehicle (manutenção)
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


# Exemplo de aplicação
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
# Saída:
# Total Bus fare is: 5500.0
