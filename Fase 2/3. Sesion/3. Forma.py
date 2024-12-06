""" CLASES ABSTRACTAS EN PYTHON """

from abc import ABC, abstractmethod


class Forma(ABC):

    @abstractmethod
    # definir el constructor
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circulo(Forma):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return f"El area del circulo es {3.14 * (self.radio**2)}"

    def perimetro(self):
        return f"El perimetro del circulo es {2 * 3.14 * self.radio}"


class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"El area del rectangulo es {self.base * self.altura}"

    def perimetro(self):
        return f"El perimetro del rectangulo es {2 * (self.base + self.altura)}"


class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f"El area del cuadrado es {self.lado**2}"


formas = [
    Circulo(5),
    Rectangulo(2, 10),
    Cuadrado(8),
    Rectangulo(10, 20),
    Circulo(22),
]

for foma in formas:
    print(foma.area())

perimCirculo = Circulo.perimetro(5)
perimRectangulo = Rectangulo.perimetro()

print(perimCirculo)
print(perimRectangulo)
