class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"Esta es una {cls.__name__}"

# Llamar a un método estático
resultado = Calculadora.sumar(5, 7)
print(resultado)  # Imprime: 12

# Llamar a un método de clase
informacion = Calculadora.info()
print(informacion)  # Imprime: Esta es una Calculadora
