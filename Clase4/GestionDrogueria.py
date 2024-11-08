ventasTotales = 0.0

# Solicitar el múmero de productos
numProductos = int(input("Ingrese el número de productos a gestionar: "))

# Listas para almacenar la información
nombres = []
precios = []
cantidades = []

print("Ingreso inicial de productos a la tienda: ")
for i in range(numProductos):
    print(f"Producto {i+1}: ")
    nombre = input("Ingrese el nombre del producto: ").lower()
    nombres.append(nombre)
    precio = float(input("Digite el precio del producto: "))
    precios.append(precio)
    cantidad = int(input("Digite la cantidad del producto: "))
    cantidades.append(cantidad)

""" Crear menú de opciones """
while True:
    print("\n ---MENU DE GESTION DROGUERIA---")
    print("1. Vender medicamento")
    print("2. Mostrar inventario")
    print("3. Mostrar ventas totales")
    print("4. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("\nVender Producto")
        nombreVenta = input("ingrese el nombre del producto a vender: ").lower()
        cantidadVender = int(input("ingrese la cantidad a vender: "))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f"Venta realizada. \nTotal de esta venta ${totalVenta:.2f}")
                    print(
                        f"Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario"
                    )
                else:
                    print(
                        f"Cantidad insuficiente en inventario, ya que en stock solo tenemos {cantidades[i]}"
                    )
                    break

        if not productoEncontrado:
            print(f'El producto "{nombre}" no se encuentra en el inventario')

    elif opcion == 2:
        print("\nInventario de productos")
        for i in range(len(nombres)):
            print(
                f"Producto {i+1}: {nombres[i].capitalize()}, precio: ${precios[i]:.2f}, cantidad: {cantidades[i]}"
            )

    elif opcion == 3:
        print(f"\nVentas totales acumuladas: ${ventasTotales:.2f}")

    elif opcion == 4:
        print("Gracias por usar el sistema de gestión de droguería dev senior")
        break

    else:

        print("Opción inválida Ingresar entre (1-4)")
