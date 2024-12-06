class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        saludo = "Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
        return saludo
