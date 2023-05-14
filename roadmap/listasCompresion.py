# listas de compresion
numeros = [1, 2, 3, 4, 5]
cuadrados = [num**2 for num in numeros]

# Impresión de los cuadrados
for cuadrado in cuadrados:
    print(cuadrado)
          
# Decorador de función
def decorador(func):
    def wrapper():
        print("Antes de llamar a la función")
        func()
        print("Después de llamar a la función")
    return wrapper

@decorador
def saludar():
    print("Hola, ¡bienvenido!")

# Llamada a la función decorada
saludar()