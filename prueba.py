# =============================
# SISTEMA DE GESTIÓN DE BIBLIOTECA
# Programación Orientada a Objetos
# =============================

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None


class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")

        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)

        print("Libro agregado correctamente")

    def agregar_miembro(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")

        miembro = Miembro(nombre, dni)
        self.miembros.append(miembro)

        print("Miembro agregado correctamente")

    def mostrar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros registrados")
            return

        print("\n--- LIBROS ---")

        for libro in self.libros:
            estado = "Disponible"

            if not libro.disponible:
                estado = f"Prestado a {libro.prestado_a.nombre}"

            print(f"Título: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"ISBN: {libro.isbn}")
            print(f"Estado: {estado}")
            print("-------------------")

    def mostrar_miembros(self):
        if len(self.miembros) == 0:
            print("No hay miembros registrados")
            return

        print("\n--- MIEMBROS ---")

        for miembro in self.miembros:
            print(f"Nombre: {miembro.nombre}")
            print(f"DNI: {miembro.dni}")

            if len(miembro.libros_prestados) == 0:
                print("No tiene libros prestados")
            else:
                print("Libros prestados:")

                for libro in miembro.libros_prestados:
                    print(f"- {libro.titulo}")

            print("-------------------")

    def prestar_libro(self):
        isbn = input("Ingrese ISBN del libro: ")
        dni = input("Ingrese DNI del miembro: ")

        libro_encontrado = None
        miembro_encontrado = None

        for libro in self.libros:
            if libro.isbn == isbn:
                libro_encontrado = libro

        for miembro in self.miembros:
            if miembro.dni == dni:
                miembro_encontrado = miembro

        if libro_encontrado is None:
            print("Libro no encontrado")
            return

        if miembro_encontrado is None:
            print("Miembro no encontrado")
            return

        if libro_encontrado.disponible:
            libro_encontrado.disponible = False
            libro_encontrado.prestado_a = miembro_encontrado
            miembro_encontrado.libros_prestados.append(libro_encontrado)

            print("Libro prestado correctamente")
        else:
            print("El libro no está disponible")

    def devolver_libro(self):
        isbn = input("Ingrese ISBN del libro a devolver: ")

        for libro in self.libros:
            if libro.isbn == isbn:

                if not libro.disponible:
                    miembro = libro.prestado_a

                    miembro.libros_prestados.remove(libro)

                    libro.disponible = True
                    libro.prestado_a = None

                    print("Libro devuelto correctamente")
                    return

        print("Libro no encontrado o ya disponible")


# =============================
# MENÚ PRINCIPAL
# =============================

biblioteca = Biblioteca()

while True:

    print("\n====== BIBLIOTECA ======")
    print("1 - Agregar libro")
    print("2 - Agregar miembro")
    print("3 - Prestar libro")
    print("4 - Devolver libro")
    print("5 - Mostrar libros")
    print("6 - Mostrar miembros")
    print("7 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        biblioteca.agregar_libro()

    elif opcion == "2":
        biblioteca.agregar_miembro()

    elif opcion == "3":
        biblioteca.prestar_libro()

    elif opcion == "4":
        biblioteca.devolver_libro()

    elif opcion == "5":
        biblioteca.mostrar_libros()

    elif opcion == "6":
        biblioteca.mostrar_miembros()

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")