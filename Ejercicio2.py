# Sistema de Gestión de Facultad

class Estudiante:
    contador_id = 1

    def __init__(self, nombre, apellido, matricula, carrera):
        self.id = Estudiante.contador_id
        Estudiante.contador_id += 1

        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos_inscriptos = []

    def inscribirse_curso(self, curso):
        if curso.inscribir_estudiante(self):
            self.cursos_inscriptos.append(curso)

    def darse_baja_curso(self, curso):
        if curso in self.cursos_inscriptos:
            curso.dar_baja_estudiante(self)
            self.cursos_inscriptos.remove(curso)
        else:
            print(f"{self.nombre} no está inscripto en este curso")

    def mostrar_cursos(self):
        print(f"\nCursos de {self.nombre} {self.apellido}:")

        if len(self.cursos_inscriptos) == 0:
            print("No está inscripto en cursos")
        else:
            for curso in self.cursos_inscriptos:
                print(f"- {curso.nombre}")


class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad_maxima):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        if len(self.estudiantes) < self.capacidad_maxima:
            self.estudiantes.append(estudiante)
            print(f"{estudiante.nombre} se inscribió en {self.nombre}")
            return True
        else:
            print(f"No hay cupos disponibles en {self.nombre}")
            return False

    def dar_baja_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
            print(f"{estudiante.nombre} se dio de baja de {self.nombre}")

    def mostrar_estado(self):
        cupos_disponibles = self.capacidad_maxima - len(self.estudiantes)

        print(f"\nCurso: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Profesor: {self.profesor}")
        print(f"Inscriptos: {len(self.estudiantes)}")
        print(f"Cupos disponibles: {cupos_disponibles}")

        if len(self.estudiantes) > 0:
            print("Estudiantes inscriptos:")

            for estudiante in self.estudiantes:
                print(f"- {estudiante.nombre} {estudiante.apellido}")


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado correctamente")

    def agregar_curso(self, curso):
        self.cursos.append(curso)
        print(f"Curso {curso.nombre} agregado correctamente")

    def mostrar_cursos(self):
        print("\n----- CURSOS -----")

        for curso in self.cursos:
            curso.mostrar_estado()

    def mostrar_estudiantes(self):
        print("\n----- ESTUDIANTES -----")

        for estudiante in self.estudiantes:
            print(f"\nID: {estudiante.id}")
            print(f"Nombre: {estudiante.nombre} {estudiante.apellido}")
            print(f"Matrícula: {estudiante.matricula}")
            print(f"Carrera: {estudiante.carrera}")

            if len(estudiante.cursos_inscriptos) == 0:
                print("No está inscripto en cursos")
            else:
                print("Cursos inscriptos:")

                for curso in estudiante.cursos_inscriptos:
                    print(f"- {curso.nombre}")


facultad = Facultad()

est1 = Estudiante("Juan", "Perez", "2023001", "Ingeniería")
est2 = Estudiante("Maria", "Gomez", "2023002", "Medicina")
est3 = Estudiante("Lucas", "Fernandez", "2023003", "Derecho")

facultad.agregar_estudiante(est1)
facultad.agregar_estudiante(est2)
facultad.agregar_estudiante(est3)

curso1 = Curso("Programación", "PRG101", "Carlos Lopez", 2)
curso2 = Curso("Matemática", "MAT201", "Ana Torres", 3)

facultad.agregar_curso(curso1)
facultad.agregar_curso(curso2)

est1.inscribirse_curso(curso1)
est2.inscribirse_curso(curso1)
est3.inscribirse_curso(curso1)

est1.inscribirse_curso(curso2)
est3.inscribirse_curso(curso2)

facultad.mostrar_cursos()
facultad.mostrar_estudiantes()

est1.darse_baja_curso(curso1)
print("\n----- ESTADO ACTUALIZADO -----")

facultad.mostrar_cursos()
facultad.mostrar_estudiantes()