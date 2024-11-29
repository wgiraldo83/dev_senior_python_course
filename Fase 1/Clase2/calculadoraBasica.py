# Ejercicios
# CALCULADORA=> Escribe unprograma que soicite dos números al usuario y realice las operaciones matemáticas SUMA, RESTA, MULTIPLICACIÓN Y DIVISIÓN

# Definimos una función para validar si el número ingresado es decimal


def es_flotante(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


inpuntUsuario = input("Ingrese el primero número: ")

esEntero = inpuntUsuario.isnumeric()
esDecimal = inpuntUsuario.isdecimal()
if not es_flotante:
    inpuntUsuario = input("El número no es válido,ingrese el primer número de nuevo: ")

numero1 = inpuntUsuario
numero2 = input("Ingrese el segundo número: ")

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma=> {suma}")
print(f"Resta=> {resta}")
print(f"Mult=> {multiplicacion}")
print(f"Div=> {division}")
