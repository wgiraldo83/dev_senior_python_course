# Metodos de clase
class AnimalII:

    qantityAnimals = 0

    def __init__(self, name):
        self.name = name
        AnimalII.qantityAnimals += 1

    @classmethod
    def totalAnimals(cls):
        return f"tengo {cls.qantityAnimals} animales"


animalito1 = AnimalII("Ron")
animalito2 = AnimalII("Rayo")
animalito3 = AnimalII("Tobi")

print(animalito1.name)
print(animalito2.name)
print(animalito3.name)
print(AnimalII.totalAnimals())
