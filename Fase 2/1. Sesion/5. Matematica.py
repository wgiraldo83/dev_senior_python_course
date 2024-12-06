# Static methods
class Math:

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b


print(f"La suma es: {Math.suma(10, 10)}")
print(f"La resta es: {Math.resta(10, 5)}")
