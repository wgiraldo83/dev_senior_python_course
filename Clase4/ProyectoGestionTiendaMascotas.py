from datetime import datetime

# Variables temporales
inventario = [
    ["Pelota", "Juguete", 500, 20, "2023-05-15"],
    ["Bola espacial", "Juguete", 300, 30, "2023-05-16"],
    ["Correa", "Accesorio", 400, 10, "2023-05-17"],
]
ventas = []
ventasTotalesAcumuladas = 0

while True:
    print("---MENU DE GESTION DE MASCOTAS DEVSENIOR---")
    print("1. Agregar un producto al inventario")
    print("2. Vender un producto")
    print("3. Mostrar el inventario detallado")
    print("4. Historia de ventas")
    print("5. Mostrar ventas totales")
    print("6. Salir")

    opcion = input("Selecciones una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        fechaIngreso = datetime.now().strftime("%Y-%m-%d")
        producto = [nombre, categoria, precio, cantidad, fechaIngreso]
        inventario.append(producto)

    elif opcion == "2":
        print("VENTAS DE PRODUCTOS")
        nombre = input("Ingrese el nombre del producto").lower()
        cantidadVender = int(input("Ingrese la cantidad a vender"))
        productoEncontrado = False
        for producto in inventario:
            if producto[0] == nombre:
                productoEncontrado = True
                if producto[3] >= cantidadVender:
                    total = producto[2] * cantidadVender
                    ventas.append([nombre, cantidadVender, total])
                    ventasTotalesAcumuladas += total
                    print("Se ha vendido el producto")
                else:
                    print("No hay suficientes productos en inventario")
                break
        if not productoEncontrado:
            print(f"El producto {nombre} no se encuentra en inventario")

    elif opcion == "3":
        if inventario:
            for producto in inventario:
                print(f"Nombre: {inventario[0]}")
                print(f"Categoría: {inventario[1]}")
                print(f"Precio: {inventario[2]}")
                print(f"Cantidad: {inventario[3]}")
                print(f"Fecha de ingreso: {inventario[4]}")
                print("---------------------------")

    elif opcion == "4":
        if ventas:
            print("--------------------")
            print("Historia de ventas")
            print("--------------------")
            for venta in ventas:
                print(f"Nombre: {venta[0]}")
                print(f"Cantidad vendida: {venta[1]}")
                print(f"Fecha de venta: {venta[3]}")
                print(f"Total vendido: {venta[2]}")
                print("--------------------")
        else:
            print("no hay ventas registradas")

    elif opcion == "5":
        if ventasTotalesAcumuladas > 0:
            print(f"Las ventas totales son: {ventasTotalesAcumuladas}")
        else:
            print("No hay ventas registradas")

    elif opcion == "6" or opcion == "salir":
        print("Gracias por usar el sistema de gestión de mascotas dev senior")
        break
    else:
        print("Opción inválida, por favor ingrese una opción entre 1 y 6")
