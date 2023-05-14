# clase ejemplo
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)


# Creación de objetos
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Acceso a atributos
print(persona1.nombre)  # Salida: Juan
print(persona2.edad)  # Salida: 25

# Llamada a métodos
persona1.saludar()  # Salida: Hola, mi nombre es Juan
persona2.saludar()  # Salida: Hola, mi nombre es María
