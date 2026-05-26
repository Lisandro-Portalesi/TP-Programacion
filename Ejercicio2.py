# EJERCICIO DE GESTIÓN DE FACULTAD

class Estudiante:

    contador_id = 1

    def __init__(self, nombre, apellido, matricula, carrera):

        self.id = Estudiante.contador_id
        Estudiante.contador_id += 1

        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos = []


class Curso:

    def __init__(self, nombre, codigo, profesor, capacidad):

        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes = []

class Facultad:

    def __init__(self):

        self.estudiantes = []
        self.cursos = []

    def agregar_estudiante(self):

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        matricula = input("Matrícula: ")
        carrera = input("Carrera: ")

        estudiante = Estudiante(nombre, apellido, matricula, carrera)

        self.estudiantes.append(estudiante)

        print("Estudiante agregado correctamente")

    def agregar_curso(self):

        nombre = input("Nombre del curso: ")
        codigo = input("Código: ")
        profesor = input("Profesor: ")
        capacidad = int(input("Capacidad máxima: "))

        curso = Curso(nombre, codigo, profesor, capacidad)

        self.cursos.append(curso)

        print("Curso agregado correctamente")

    def mostrar_cursos(self):

        if len(self.cursos) == 0:
            print("No hay cursos registrados")
            return

        print("\n--- CURSOS ---")

        for curso in self.cursos:

            cupos = curso.capacidad - len(curso.estudiantes)

            print(f"Curso: {curso.nombre}")
            print(f"Código: {curso.codigo}")
            print(f"Profesor: {curso.profesor}")
            print(f"Inscriptos: {len(curso.estudiantes)}")
            print(f"Cupos disponibles: {cupos}")

            if len(curso.estudiantes) > 0:
                print("Estudiantes:")

                for estudiante in curso.estudiantes:
                    print(f"- {estudiante.nombre} {estudiante.apellido}")

            print("-------------------")

    def mostrar_estudiantes(self):

        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados")
            return

        print("\n--- ESTUDIANTES ---")

        for estudiante in self.estudiantes:

            print(f"ID: {estudiante.id}")
            print(f"Nombre: {estudiante.nombre} {estudiante.apellido}")
            print(f"Matrícula: {estudiante.matricula}")
            print(f"Carrera: {estudiante.carrera}")

            if len(estudiante.cursos) == 0:
                print("No está inscripto en cursos")

            else:
                print("Cursos inscriptos:")

                for curso in estudiante.cursos:
                    print(f"- {curso.nombre}")

            print("-------------------")

    def inscribir_estudiante(self):

        matricula = input("Ingrese matrícula del estudiante: ")
        codigo = input("Ingrese código del curso: ")

        estudiante_encontrado = None
        curso_encontrado = None

        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                estudiante_encontrado = estudiante

        for curso in self.cursos:
            if curso.codigo == codigo:
                curso_encontrado = curso

        if estudiante_encontrado is None:
            print("Estudiante no encontrado")
            return

        if curso_encontrado is None:
            print("Curso no encontrado")
            return

        if len(curso_encontrado.estudiantes) < curso_encontrado.capacidad:

            curso_encontrado.estudiantes.append(estudiante_encontrado)
            estudiante_encontrado.cursos.append(curso_encontrado)

            print("Inscripción realizada correctamente")

        else:
            print("No hay cupos disponibles")

    def dar_baja(self):

        matricula = input("Ingrese matrícula del estudiante: ")
        codigo = input("Ingrese código del curso: ")

        for estudiante in self.estudiantes:

            if estudiante.matricula == matricula:

                for curso in estudiante.cursos:

                    if curso.codigo == codigo:

                        estudiante.cursos.remove(curso)
                        curso.estudiantes.remove(estudiante)

                        print("Baja realizada correctamente")
                        return

        print("No se encontró la inscripción")


# MENÚ PRINCIPAL

facultad = Facultad()

while True:

    print("\n====== FACULTAD ======")
    print("1 - Agregar estudiante")
    print("2 - Agregar curso")
    print("3 - Inscribir estudiante")
    print("4 - Dar baja de curso")
    print("5 - Mostrar cursos")
    print("6 - Mostrar estudiantes")
    print("7 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        facultad.agregar_estudiante()

    elif opcion == "2":
        facultad.agregar_curso()

    elif opcion == "3":
        facultad.inscribir_estudiante()

    elif opcion == "4":
        facultad.dar_baja()

    elif opcion == "5":
        facultad.mostrar_cursos()

    elif opcion == "6":
        facultad.mostrar_estudiantes()

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")