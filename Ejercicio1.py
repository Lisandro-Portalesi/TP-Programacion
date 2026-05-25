# Sistema de Gestión de Biblioteca

class Libro:
    def _init_(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None

    def prestar(self, miembro):
        if self.disponible:
            self.disponible = False
            self.prestado_a = miembro
            print(f"El libro '{self.titulo}' fue prestado a {miembro.nombre}")
        else:
            print(f"El libro '{self.titulo}' no está disponible")

    def devolver(self):
        if not self.disponible:
            print(f"El libro '{self.titulo}' fue devuelto")
            self.disponible = True
            self.prestado_a = None
        else:
            print(f"El libro '{self.titulo}' ya está disponible")

    def mostrar_estado(self):
        if self.disponible:
            print(f"'{self.titulo}' - Disponible")
        else:
            print(f"'{self.titulo}' - Prestado a {self.prestado_a.nombre}")


class Miembro:
    def _init_(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.prestar(self)
            self.libros_prestados.append(libro)
        else:
            print("No se puede realizar el préstamo")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print(f"{self.nombre} no tiene prestado este libro")

    def mostrar_libros(self):
        print(f"\nLibros prestados por {self.nombre}:")

        if len(self.libros_prestados) == 0:
            print("No tiene libros prestados")
        else:
            for libro in self.libros_prestados:
                print(f"- {libro.titulo}")


class Biblioteca:
    def _init_(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente")

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
        print(f"Miembro '{miembro.nombre}' agregado correctamente")

    def mostrar_libros(self):
        print("\nEstado de los libros:")

        for libro in self.libros:
            libro.mostrar_estado()

    def mostrar_miembros(self):
        print("\nEstado de los miembros:")

        for miembro in self.miembros:
            print(f"\nNombre: {miembro.nombre}")
            print(f"DNI: {miembro.dni}")

            if len(miembro.libros_prestados) == 0:
                print("No tiene libros prestados")
            else:
                print("Libros prestados:")

                for libro in miembro.libros_prestados:
                    print(f"- {libro.titulo}")

biblioteca = Biblioteca()


libro1 = Libro("1984", "George Orwell", "123")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "456")
libro3 = Libro("Don Quijote", "Miguel de Cervantes", "789")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

miembro1 = Miembro("Juan Perez", "40111222")
miembro2 = Miembro("Maria Gomez", "38999111")

biblioteca.agregar_miembro(miembro1)
biblioteca.agregar_miembro(miembro2)

miembro1.tomar_prestado(libro1)
miembro2.tomar_prestado(libro2)

biblioteca.mostrar_libros()
biblioteca.mostrar_miembros()

miembro1.devolver_libro(libro1)
print("\n--- Estado actualizado ---")

biblioteca.mostrar_libros()
biblioteca.mostrar_miembros()