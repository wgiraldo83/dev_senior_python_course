paises = ("Colombia", "Mexico", "Ecuador", "Venezuela")
print(type(paises))  # Imprimo el tipo de archivo

# Conocer el tamaño
print("\nConocer el tamaño")
print(len(paises))

# Imprimir sólo un elemento específico
print("\nImprimir sólo un elemento específico")
print(paises[2])  # Con esto imprimo Ecuador que está en la segunda posición de la tupla

# Imprimir el último elemento de la lista
print("\nImprimir el último elemento de la lista")
print(paises[-1])

# Imprimir los elemento uno por fila
print("\nImprimir los elemento uno por fila")
for pais in paises:
    print(pais)
