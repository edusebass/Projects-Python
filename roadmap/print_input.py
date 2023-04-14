

                                        #PRINT AND INPUT
# Ejercicio 1
# Realice un algoritmo, represéntelo mediante un diagrama de flujo y el
# pseudocódigo respectivo, para ir al cine.

print("Paso 1: Salir de la casa")
print("Paso 2: Seleccionar la pelicula")
print("Paso 3: Pagar la entrada")
print("Paso 4: Ver la pelicula")
print("Paso 5: Regresar a la casa")
print("=========================================================================")


  # Ejercicio 2
# Un estudiante realiza cuatro exámenes durante el semestre, los cuales tienen
# diferentes ponderaciones. Realice el pseudocódigo, el diagrama de flujo y
# programa que representen el algoritmo correspondiente para obtener el
# promedio de las calificaciones obtenido

  #dECLARA TUS CONSTANTES
CALIFI = 4
  #DECLARA TUS VARIABLES
C1 = 0
C2 = 0
C3 = 0
C4 = 0
suma = 0.0
promedio = 0.0
  #SOLICITA DATOS AL USUARIO
print("Ingresa las cuatro calificaciones: ")
c1 = float(input())
c2 = float(input())
c3 = float(input())
c4 = float(input())
  #REALIZA EL PROCEDIMIENTO
suma = c1 + c2 + c3 + c4
promedio = suma / CALIFI
  IMPRIME LOS RESULTADOS
print("La suma de las calificaciones: ", suma)
print("El promedio de las calificaciones: ", promedio)
print("Si el promedio es mayor a 14 pasas, caso contrario perdiste😢")

print("================================================================")


  # Ejercicio 3
# Una florería requiere la implementación de un programa para poder realizar el proceso de
# facturación de las ventas. Realice el pseudocódigo, el diagrama de flujo y programa que
# representen el algoritmo correspondiente para obtener el detalle de la compra de las rosas. En
# base a la siguiente tabla 

  #SOLICITA DATOS AL USUARIO
nombre = input("Ingrese su nombre: ")
correo = input ("Ingrese su correo: ")
cedula = input ("Ingrese su cedula: ")
telefono = input ("Ingrese su telefono: ")
print("Ingresar el numero de flores para el arreglo floral")
floresrojas = int(input("rosas: "))
girasoles = int(input("girasoles: "))
claveles = int(input("claveles: "))
dalias = int(input("dalias: "))
suma = floresrojas + girasoles + claveles + dalias
print("--------------------------------> La suma de flores es: ", suma)
  #REALIZA EL PROCEDIMIENTO
cantidadRojas = floresrojas * 0.75
cantidadGirasoles = girasoles * 0.50
cantidadClaveles = claveles * 1.25
cantidadDalias = dalias * 1.12
total = cantidadRojas + cantidadGirasoles + cantidadClaveles + cantidadDalias
pagoconIva = total * 1.12
  #IMPRIME LOS RESULTADOS
print("------------------------FACTURA DE VENTA------------------------")
print("Nombre: ", nombre, " ")
print("Correo: ", correo, " ")
print("Cedula: ", cedula, " ")
print("Telefono: ", telefono, " ")
print("----------------------------------------------------------------")
print("\t\t PRODUCTO \t\t\t\t\t CANTIDAD")
print("Flores Rojas \t\t\t\t\t\t\t ", floresrojas)
print("Girasoles \t\t\t\t\t\t\t\t ", girasoles)
print("Claveles \t\t\t\t\t\t\t\t ", claveles)
print("Dalias \t\t\t\t\t\t\t\t\t ", dalias)
print("\t\t\t\t\t\t\t\t Pago con iva: ", round(pagoconIva, 2))


