import random

# Generar un número aleatorio entre 1 y 10
numeroSecreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza == numeroSecreto:
        print("¡Felicidades! Has adivinado el número 🎇")
        adivinado = True
    elif adivinanza < numeroSecreto:
        print("El número es mayor 📈")
    else:
        print("El número es menor 📉")
