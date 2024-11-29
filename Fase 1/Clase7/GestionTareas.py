from datetime import datetime
import statistics


class Tarea:
    # Función de inicialización = método constructor
    def __init__(self, nombreTarea, fechaLimite, categoria, horasDedicadas):

        # Variables          parámetros
        self.nombreTarea = nombreTarea
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        self.horasDedicadas = horasDedicadas


# Función para agregar una tarea
def agregarUnaTarea(listaTareas):
    nombreTarea = input("Ingrese el nombre de la tarea: ")
    fechaLimite_str = input("Ingrese la fecha límite de la tarea: ")
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no vpalida, el formato es (DD/MM/YYYY)")
        return
    categoria = input(
        "Ingrese la categoría de la tarea (Estudio, Trabajo, Personal, Etc): "
    )
    horasDedicadas_str = input("Ingrese las horas separadas por coma, ejm 3,4,5: ")
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print("Horas no válidas")
        return

    # Crear un objeto y lo agrega a la lista de tareas
    tarea = Tarea(nombreTarea, fechaLimite, categoria, horasDedicadas)
    listaTareas.append(tarea)


def visualizarTareas(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombreTarea}")
        print(f'Fecha límite: {tarea.fechaLimite.strftime("%d/%m/%Y")}')
        print(f"Categoría: {tarea.categoria}")
        print(f"Horas dedicadas: {tarea.horasDedicadas}")


# Función para generar el análisis de las horas dedicadas a las tareas
def analizarHoras(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas")
        return

    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f"\nAnálisis de {tarea.nombreTarea}")
        print(f"Promedio de horas: {promedio}")
        print(f"Máximo de horas: {maximo}")
        print(f"Mínimo de horas: {minimo}")


# Función para genera el informa
def generarInforme(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas")
        return

    # Crerar y abrir un archivo txt
    with open("Informe tareas.txt", "w") as archivo:
        # Escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f"Nombre: {tarea.nombreTarea}\n")
            archivo.write(f'Fecha límite: {tarea.fechaLimite.strftime("%d/%m/%Y")}\n')
            archivo.write(f"Categoría: {tarea.categoria}\n")
            archivo.write(f"Horas dedicadas: {tarea.horasDedicadas}\n")
            archivo.write("\n")
    print("Informe generado como 'Informe tareas.txt'")


# Crear el menú para que el usuario interactúe con el programa
def menu():
    listaTareas = []
    while True:
        print("\nMenú de opciones")
        print("\n1. Agregar tarea")
        print("\n2. Visualizar tareas")
        print("\n3. Analizar horas dedicadas")
        print("\n4. Generar informe")
        print("\n5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregarUnaTarea(listaTareas)
        elif opcion == "2":
            visualizarTareas(listaTareas)
        elif opcion == "3":
            analizarHoras(listaTareas)
        elif opcion == "4":
            generarInforme(listaTareas)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
