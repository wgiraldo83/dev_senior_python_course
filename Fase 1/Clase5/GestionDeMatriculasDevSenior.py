# Definir listas
estudiantes = []
cursos = ["Java", "Python"]
docentes = []
horarios = []


# Función para matricular un estudiante
def matricularEstudiante():
    nombre = input("Digite el nombre del estudiante: ")
    print("Seleccione el curso a matricular: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")

    cursoSeleccionado = int(input("Ingrese el número del curso: "))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]

        # Creamos un dicionario llamado estudiante
        estudiante = {"nombre": nombre, "curso": curso}
        # Guardo el estudiante en la lista estudiantes
        estudiantes.append(estudiante)
        print(f"Estudiante: {nombre}, marticulado en el curso: {curso}")
    else:
        print(
            f"La opción seleccionada no es válida, seleccione un número entre 1 y {len(cursos)}"
        )


# Función para asignar un docente a un curso
def asignarDocente():
    print("Seleccione el curso al que desea asignar el docente: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")

    cursoSeleccionado = int(input("Ingrese el número del curso: "))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        nombreDocente = input("Ingrese el nombre del docente: ")

        # Creamos un dicionario llamado docente
        docente = {"nombre": nombreDocente, "curso": curso}
        # Guardo el estudiante en la lista estudiantes
        docentes.append(docente)
        print(f"Docente: {nombreDocente}, asignado al curso: {curso}")
    else:
        print(
            f"La opción seleccionada no es válida, seleccione un número entre 1 y {len(cursos)}"
        )


# Función para asignar horario a un curso
def asignarHorario():
    print("Seleccione el curso al que desea asignar el  horario: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")

    cursoSeleccionado = int(input("Ingrese el número del curso: "))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        dias = input("Ingrese los días de clase (ejm: martes y jueves): ")
        hora = input("Ingrese la hora de la clase (ejm: 6 pm):")

        # Creamos un dicionario llamado horario
        horario = {"curso": curso, "días": dias, "hora": hora}
        # Guardo el estudiante en la lista estudiantes
        horarios.append(horario)
        print(f"Horario asignado al curso: {curso}: {dias} a las {hora} ")
    else:
        print(
            f"La opción seleccionada no es válida, seleccione un número entre 1 y {len(cursos)}"
        )


# Función para mostrar los estudiantes matriculados
def mostrarEstudiantes():
    if estudiantes:
        print("Lista de estudiantes matriculados")
        for estudiante in estudiantes:
            print(f"Estudiante: {estudiante['nombre']}, Curso: {estudiante['curso']}")
    else:
        print("No hay estudiantes matriculados")


# Función para mostrar los docentes asignados
def mostrarDocentes():
    if docentes:
        print("Lista de docentes asignados")
        for docente in docentes:
            print(f"Docente: {docente['nombre']}, Curso: {docente['curso']}")
    else:
        print("No hay docentes asignados")


# Función para mostrar los docentes asignados
def mostrarHorarios():
    if horarios:
        print("\nHorarios de los cursos")
        for horario in horarios:
            print(
                f"Curso: {horario['curso']}, Días: {horario['dias']}, Hora: {horario['hora']}"
            )
    else:
        print("No hay horarios asignados")


while True:
    print("\n Sistema de matrículas de Dev Senior")
    print("1. Matricular estudiante ")
    print("2. Asignar docente a un curso ")
    print("3. Asignar horario a un curso ")
    print("4. Mostrar la lista de estudiantes matriculados ")
    print("5. Mostrar la lista de docentes asignados ")
    print("6. Mostrar horarios de los cursos ")
    print("7. Salir ")

    opcion = int(input("Digite la opción: "))

    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrarEstudiantes()
    elif opcion == 5:
        mostrarDocentes()
    elif opcion == 6:
        mostrarHorarios()
    elif opcion == 7:
        print("Gracias por utilizar  el sistema de matrículas")
        break
    else:
        print("Opción inválida, debe seleccionar una de las opciones del menú")
