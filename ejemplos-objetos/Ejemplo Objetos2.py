class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

# Crear un objeto de la clase Libro
libro1 = Libro("1984", "George Orwell")
libro1.mostrar_info()  # Imprime: Título: 1984, Autor: George Orwell

# Modificar el atributo 'titulo'
libro1.titulo = "Rebelión en la granja"
libro1.mostrar_info()  # Imprime: Título: Rebelión en la granja, Autor: George Orwell
