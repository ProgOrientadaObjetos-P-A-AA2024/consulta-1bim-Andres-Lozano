class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
persona1.mostrar_informacion()
