conceptosProgramacion = {
    "POO": "Programación Orientada a Objetos",
    "IDE": "Entorno de Desarrollo Integrado",
    "DBMS": "Sistema de Gestión de Bases de Datos",
}
print(type(conceptosProgramacion))
print(conceptosProgramacion)

# Imprimir el tamaño del diccionario
print("\nImprimir el tamaño del diccionario")
print(len(conceptosProgramacion))

# Imprimir un dato específico
print("\nImprimir un dato específico")
print(conceptosProgramacion["IDE"])  # Especificando la clave
print(conceptosProgramacion.get("POO"))  # Especificando la clave

# Modificar un valor específico
print("\nModificar un valor específico")
conceptosProgramacion["DBMS"] = "Database Management Systems"
print(conceptosProgramacion)

# Imprimir las claves (ID) un elemento por fila
print("\nImprimir las claves (ID) un elemento por fila")
for key in conceptosProgramacion:
    print(key)

# Imprimir las parejas un elemento por fila
print("\nImprimir las parejas un elemento por fila")
for key, value in conceptosProgramacion.items():
    print(f"{key} : {value}")
