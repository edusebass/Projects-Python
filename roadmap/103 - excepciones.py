#excepciones
#  resultado = 10 / 0 #nos sale error y se detiene el programa

#try 
#except
#finally

#-----------
try:
    resultado = 10 / 0
except: #podemos agregar excepciones especificas
    print("No se puede dividir para cero")

# ZeroDivisionError: Se produce cuando se intenta dividir un número por cero.
try:
    resultado = 10 / 0
except ZeroDivisionError: #podemos agregar excepciones especificas
    print("No se puede dividir para cero")

# TypeError: Ocurre cuando se intenta realizar una operación utilizando objetos de tipos incompatibles.
try:
    resultado = "10" + 5
except TypeError:
    print("Error: No se puede concatenar una cadena y un entero.")

# ValueError: Se lanza cuando una función recibe un argumento con el tipo correcto pero un valor incorrecto.
try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir 'abc' a un entero.")

#FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("Error: El archivo no se encontró.")


#finally

try:
    resultado = 10 / 2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
finally:
    print("Operación finalizada.")









