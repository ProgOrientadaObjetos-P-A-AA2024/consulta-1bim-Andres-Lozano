class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

# Crear una instancia de la clase Coche
coche1 = Coche("Toyota", "Corolla", 2020)
coche1.mostrar_detalles()
