nombres = ["Juan", "Sebastian", "Melissa", "Xiomara"]
# Imprimir el tipo de arreglo
print(type(nombres))

# Imprimir el dato en una posición específica
print(nombres[1])  # Para imprimir a Sebastian

# Para imprimir el último dato de la lista
print(nombres[-1])

# Rangos en las colecciones
print(nombres[0:2])  # Se puede omitir el 0 y poner [:2] y funcionará igual
print(
    nombres[2:]
)  # Si no ppongo nada a la derecha de los ":", imprimirá desde el punto de partida hasta el final de la colección

# Para conocer la cantidad de elementos de la lista
print("\nPara conocer la cantidad de elementos de la lista")
print(len(nombres))

# Para adicionar un elemento al final de la lista
print("\nPara adicionar un elemento al final de la lista")
nombres.append("Elizabeth")
print(nombres)

# Para insertar un elemento en una posición específica
print("\nInserto a María en la segunda posición de la lista")
nombres.insert(1, "María")  # Inserto a María en la segunda posición de la lista
print(nombres)

# Para eliminar un elemento de la lista
print("\nElimina el elemento especificado")
nombres.remove("Elizabeth")  # Elimina el elemento especificado
print(nombres)

print("\nElimina el último elemento de la lista")
nombres.pop()  # Elimina el último elemento de la lista
print(nombres)

print("\nElimina un elemento específico de la lista")
nombres.pop(1)  # Elimina un elemento específico de la lista
print(nombres)

print("\nElimina según el índice especificado")
del nombres[1]  # Elimina según el índice especificado
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres)  # Esto me dará un error porque la lista ya fue eliminada
