# Polimorfismo
class Animal:
    def __init__(self):
        pass

    def speak(self):
        pass


class Dog(Animal):

    def __init__(self):
        pass

    def speak(self):
        return f"El perro dice woof woof"


class Cat(Animal):
    def __init__(self):
        pass

    def speak(self):
        return f"El gato dice meow meow"


# Creo una lista para llamar el método speak
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
