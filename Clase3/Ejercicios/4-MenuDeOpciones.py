opcion = 0
while opcion != 3:
    opcion = int(
        input("Seleccione una opción:\n1) Saludar\n2) Despedirse\n3) Salir\n\n")
    )
    if opcion == 1:
        print("Hola alumno de python")
    elif opcion == 2:
        print("Adios")
    elif opcion == 3:
        print("Has salido de la aplicación")
    else:
        print("La opción ingresada no es correcta, intenta de nuevo")
