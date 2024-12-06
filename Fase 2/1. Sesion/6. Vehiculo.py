class Vehiculo:
    def __init__(self, type):
        self.type = type

    def description(self):
        return f"Este vehiculo es de tipo {self.type}"


class Motorcycle(Vehiculo):

    def __init__(self, type, make):
        super().__init__(type)
        self.make = make


Motorcycle1 = Motorcycle("moto", "Ducatti")
print(Motorcycle1.description())
