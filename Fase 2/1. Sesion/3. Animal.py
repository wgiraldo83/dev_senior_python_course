class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        message = f"Mi animalito se llama {self.name} y tiene {self.age} años."
        return message


animal1 = Animal("Ginebra", 3)

print(animal1.name)
print(animal1.age)
print(animal1.speak())
