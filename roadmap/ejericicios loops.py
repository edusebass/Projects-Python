# EJERCICIO 4

sumacali = 0.0
calificacion = 0
for i in range (1, 5):
  print(f'Ingrese la calificacion {i}: ')
  calificacion = float(input())
  sumacali += calificacion

promedio = sumacali/4

if promedio >= 14:
  print("APROBADO")
elif promedio <= 13 and promedio >= 9:
  print("SUPLETORIO")
elif promedio <= 8:
  print("RECHAZADO")


# EJERCICIO 5

num = int(input("Ingrese un numero: "))
if num >= 10 and num <= 100:
  print("El numero se encuentra en en le rango de 10-100")
elif num < 10 or num > 100:
  print("No se encuentra en el rango de 10-100")

# EJERCICIO 6
print("1), 2), 3), 4)")
tipo = int(input("Ingrese que tipo de tarjeta dispone: "))
cred_ant = int(input("Ingrese credito anterior: "))



if tipo == 1:
  cred_act = (cred_ant + (cred_ant * 0.25))
  print(f'Su credito actual es {cred_act}')
if tipo == 2:
  cred_act = (cred_ant + (cred_ant * 0.35))
  print(f'Su credito actual es {cred_act}')
if tipo == 3:
  cred_act = (cred_ant + (cred_ant * 0.40))
  print(f'Su credito actual es {cred_act}')
if tipo == 4:
  cred_act = (cred_ant + (cred_ant * 0.50))
  print(f'Su credito actual es {cred_act}')


# EJERCICIO 7

# En los almacenes “ETAFASHION” se van aplicar unos descuentos por el mes
# del padre en el que se rebaja el 10% del precio total de la compra si se adquieren
# más de 20 unidades y 5% si adquieren hasta 20 unidades, pero más de 10. Por
# otra parte, no hay descuento para cantidades menores o iguales a 9 unidades.
# Con el precio total de la compra y la cantidad adquirida de prendas realice un
# programa, para mostrar el nuevo valor pagar y la cantidad de prendas de vestir
# adquiridas.
prendas = int(input("Ingrese el numero de prendas: "))
while prendas<=0:
  print("Debe ingresar un número válido de prendas")
  prendas = int(input("Ingrese el número de prendas: "))
valor = float(input("Ingrese el valor total: "))

if prendas > 20:
  valor = valor - (valor * 0.10)
  print(f"Su valor ahora es: {valor}")
  
elif prendas < 20 and prendas > 10: 
  valor = valor - (valor * 0.05)
  print(f"Su valor ahora es: {valor}")
elif prendas <= 9:
  print(f"No hay descuento, su valor ahora es: {valor}")

# EJERCICIO 8
print("------------------- LA UNIÓN  ---------------")

numguaguas = int (input("Ingrese el numero de guaguas: "))
sumaguaguas = 0
sumamoras = 0
contadorguaguas = 0
while  contadorguaguas < numguaguas:
  precioguagua = float(input(f"Ingrese el precio de la guagua #{contadorguaguas + 1}: ")) #el + 1 es para que te aparesca el 1
  sumaguaguas += precioguagua
  print("La guagua es de mora?")
  tipoguagua = str(input("si o no?"))
  if tipoguagua == "si":
    sumamoras += 1
  contadorguaguas += 1
  
print("El numero de guaguas es: ", numguaguas)
print (f"El precio del total de guaguas es: {sumaguaguas}")
print(f"Las que son de moras son: {sumamoras}")

#EJERCICIO 9
print("------------------- EPN  ---------------")
numemple = int(input("Ingrese el numero de empleados: "))
contsueldo = 0.0
numhoras = 0
sumprofes = 0
sumnumemple = 0
conthoras = 0

while sumnumemple < numemple:
  sueldoemple = float(input(f"Ingrese el sueldo del empleado {sumnumemple + 1}: "))
  contsueldo += sueldoemple
  horasemple = int(input("Cuantas horas trabaja: "))
  conthoras += horasemple
  esprofe = str(input("Es profesor?\nsi o no?: "))
  if esprofe == "si":
    sumprofes += 1
  sumnumemple += 1

print(f"La cantidad de empleados son: {numemple}")
print(f"El total de sueldos de todos los empleados es: {contsueldo}")
print(f"El total de horas de todos los empleados es: {conthoras}")
print(f"El total de empleados que son profesores es: {sumprofes}")

#EJERCICIO 10
print("1)Lavar ropa")
print("2)Limpiar espejo")
print("3)Planchar")
print("4)Compras")
print("5)Playa")
print("6)Excursion")
print("7)Piscina")
print("8)Cine")
print("9)Danza")
opcion = int(input("Ingrese el numero de la opcion: "))

while opcion < 1 or opcion > 9:
  opcion = int(input("Error. Ingrese el numero de la opcion, otra vez: "))