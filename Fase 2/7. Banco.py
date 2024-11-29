# Combinando métodos estáticos con y métodos de clase
class Banco:
    rate = 0.03

    def __init__(self, name):
        self.name = name

    @classmethod
    def chageRate(cls, rate):
        cls.rate = rate

    @classmethod
    def convertDollarsToEuro(dollars):
        return dollars * (1 + Banco.rate)
