'''Crea un programa que simule el funcionamiento de un cajero automático. 
El cajero debe comenzar con un saldo inicial de $1000 y permitir al usuario elegir entre las siguientes opciones: 
ingresar dinero en la cuenta, 
retirar dinero de la cuenta, 
mostrar el dinero disponible o 
salir del programa.'''

saldo = 1000

print("----------MENU-----------")
print("Binevenido a tu cajero automatico")
print("1. Ingresar dinero a la cuenta")
print("2. Restirar dinero de la cuenta")
print("3. Mostrar dinero de la cuenta")
print("4. Salir")

opcion = int(input("Eliga una opcion: "))

if opcion == 1:
    cantidad = float(input("Ingresa la cantidad a depositar: "))
    #operadores de asignacion
    saldo += cantidad #saldo = saldo + cantidad que ingresamos
    print("Deposito realizado correctamente, tu saldo actual es: ", saldo)

elif opcion == 2:
    cantidadRetiro = float(input("Ingresa la cantidad a retirar: "))

    if saldo >= cantidadRetiro:
        saldo -= cantidadRetiro
        print("Retiro realizado correctamente: ", saldo)
    else:
        print("Saldo insuficiente, intentalo de nuevo")

elif opcion == 3:
    print("Tu saldo actual es: ", saldo)

elif opcion >= 4 or opcion <= 0:
    print("Gracias por utilizar nuestros servicios")
