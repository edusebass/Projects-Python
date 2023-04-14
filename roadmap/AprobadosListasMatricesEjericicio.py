from os import system
def mostrarMenu():
  print("\n---------------------- MENU ----------------------")
  print("1) Calificaciones(aprobados y reprobados) ")
  print("2) Impuesto automotriz ")
  print("3) Vectores (Nombres y edades) nombre del mayor del vector")
  print("4) Multiplicar diagonal de una matriz")
  print("5) Salir ")
  opcion = int(input("\nElija que ejericio quiere realizar: "))
  return opcion

def ejercicio1():
  # Realice un algoritmo para leer las calificaciones de N alumnos y determine el número de aprobados y reprobados. 
  estudiantes = 0
  notas = 0
  reprobado = 0
  aprobado = 0
  print("\nRealice un algoritmo para leer las calificaciones de N alumnos y determine el número de aprobados y reprobados.")
  estudiantes = int(input("\nIngrese los estudiantes que tiene: "))
  for i in range(estudiantes):
    notas = int(input(f'Ingrese la nota nota del estudiante # {i + 1} :'))
    if notas < 7:
      reprobado += 1
    if notas >= 7:
      aprobado += 1
  print("Reprobados: ", reprobado)
  print("Aprobados: ", aprobado)
def ejercicio2():
#   El gerente de una compañía automotriz desea determinar el impuesto que va a pagar por cada uno de los automóviles que posee,
# además del total que va a pagar por cada categoría y por todos los
# vehículos, basándose en la siguiente clasificación:
# Los vehículos con clave 1 pagan 10% de su valor.
# Los vehículos con clave 2 pagan 7% de su valor.
# Los vehículos con clave 3 pagan 5% de su valor.
  print("\nEl gerente de una compañía automotriz desea determinar el impuesto que va a pagar por cada uno de los automóviles que posee")
  autos = int(input("Cuanto autos dispone: "))
  for i in range(autos):
    clave = int(input(f'\nIngrese la clave del vehiculo # {i +1}: '))
    valor = int(input(f'Ingrese el valor del vehiculo #{i + 1}: '))
    total = 0
    if clave == 1:
      total = valor * 0.1
    if clave == 2:
      total = valor * 0.07
    if clave == 3:
      total = valor * 0.05
    print(f'El impuesto del auto #{i + 1} es: {total}')
def ejercicio3():
  # Realice y represente mediante diagrama de flujo y pseudocódigo un algoritmo que lea los nombres y las edades de diez alumnos, y que los datos se almacenen en dos vectores, y con base en esto se determine el nombre del alumno con la edad mayor del arreglo
  nombres = []
  edades = []
  print("\nRealice y represente mediante diagrama de flujo y pseudocódigo un algoritmo que lea los nombres y las edades de diez alumnos, y que los datos se almacenen en dos vectores, y con base en esto se determineel nombre del alumno con la edad mayor del arreglo")
  for i in range(0, 10):
    nombre = str(input(f'\nIngrese el nombre del estudiante #{i +1}: '))
    edad =int(input(f'Ingrese la edad del estudiante #{i +1}: '))
    nombres.append(nombre)
    edades.append(edad)
  mayor = edades[0]
  
  for i in edades:
    if i > mayor:
      mayor = i
  j = edades.index(mayor)
  print(f'\nEl mayor es {nombres[j]}, y su edad es: {mayor}')
  
def ejercicio4():
  # Realice un algoritmo que calcule el valor que se obtiene al multiplicarentre sí los elementos de la diagonal principal de una matriz de 5 por5 elementos, represéntelo mediante diagrama, diagrama N/S y pseudocódigo
  print("\nRealice un algoritmo que calcule el valor que se obtiene al multiplicarentre sí los elementos de la diagonal principal de una matriz de 5 por5 elementos, represéntelo mediante diagrama, diagrama N/S y pseudocódigo")
  matriz = [[52, 33, 41, 56, 34],
           [55, 34, 34, 67, 89],
           [34, 56, 78, 23, 45],
           [52, 33, 41, 56, 34],
           [34, 56, 78, 23, 45]]
  print("\n")
  multi = 1
  for f in range(len(matriz)): 
    for c in range(len(matriz[f])): 
      print(f'{matriz[f][c]} ', end = "")
      if f == c:
        multi *= matriz[f][c]
    print("\n")
  print("La multiplicacion de la diagonal es: ", multi)
def main():
  opcion = mostrarMenu()
  while opcion != 5:
    if opcion == 1:
      ejercicio1()
      opcion = mostrarMenu()
    if opcion == 2:
      ejercicio2()
      opcion = mostrarMenu()
    if opcion == 3:
      ejercicio3()
      opcion = mostrarMenu()
    if opcion == 4:
      ejercicio4()
      opcion = mostrarMenu()
  system("clear")
  print("ADIOS......")   
main()