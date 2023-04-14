califiTupla = ()
califiLista = (list(califiTupla))
numCalificaciones = 0


def mostrarMenu():
  print("\n----------------SISTEMA Saew2.0------------------")
  print("1) Ingresar calificaciones")
  print("2) Mostrar calificaciones")
  print("3) Detalle de calificaciones")
  print("4) Salir")
  opcion = int(input("Ingresa la opcion: "))
  return opcion

def ingresoCalificaciones(numCalificaciones):
  
  for i in range(numCalificaciones):
    calificacion = float(input(f'Ingrese la calificaion #{i +1}: '))
    while calificacion < 0 or calificacion > 20:
      print("Error. Ingrese calificaciones entre (0 y 20)")
      calificacion = float(input(f'Ingrese la calificaion #{i +1}: '))
    califiLista.append(calificacion) 

def mostrarCalificaciones():
  print("\n-----------------------------")
  print("Las calificaciones registradas son las siguientes\n")
  califiLista.sort()
  for i in califiLista:
    print(f' [{i}] ',end="")
  
def detalleCalificaciones(numCalificaciones):
  sumaCalifi = 0
  for i in califiLista:
    sumaCalifi += i
  contadorRecha = 0
  contadorSuspen = 0
  contadorApro = 0
  for i in califiLista:
    if 1 <= i <= 8:
      contadorRecha += 1
    if 9 <= i <= 13:
      contadorSuspen += 1
    if 14 <= i <= 20:
      contadorApro += 1
        
  print("--------------------------------")
  print("Detalle de las calificaciones")
  print("* Promedio de la calificaciones es: ",(sumaCalifi / numCalificaciones))
  print("* Número de estudiantes aprobados son: ",contadorApro)
  print("* Número de estudiantes suspensos son: ",contadorSuspen)
  print("* Número de estudiantes reprobados son: ",contadorRecha)
  
def main():
  opcion = mostrarMenu()
  while opcion != 4:
    if opcion == 1:
      numCalificaciones = int(input("Ingrese cuantas calificaciones va a ingresar: "))
      ingresoCalificaciones(numCalificaciones)
      opcion = mostrarMenu()
    if opcion == 2:
      mostrarCalificaciones()
      opcion = mostrarMenu()
    if opcion == 3:
      detalleCalificaciones(numCalificaciones)
      opcion = mostrarMenu()
  print("Hasta luego")
  
main()