import random
nombres = []
huellas = []
codigos = []


def menu_opciones():
  print("Que accion desea realizar?")
  print("*1)Ingresar usuarios: ")
  print("*2)Mostrar usuarios: ")
  print("*3)Buscar usuario: ")
  print("*4)Salir: ")
  opcion = int(input("Ingrese la opcion: "))
  return opcion

def buscarUsuario():
  buscarnombre = input("Inserte el nombre para buscarlo: ")
  if buscarnombre in nombres:
    print("Si esta en el registro")
    i = nombres.index(buscarnombre)
    print("Nombre: ", nombres[i])
    print("Huella: ", huellas[i])
    print("Codigo: ", codigos[i])
  else:
    print("No esta en el registro")

def registrar(numPersonas):
  print("----------Modulo de de registro--------")
  for i in range(numPersonas):
    print(f'Ingrese los datos de la persona {i + 1}: ')
    nombreUsuario = input("Ingrese el nombre: ")
    huellaUsuario = input("Ingrese la huella: ")
    nombres.append(nombreUsuario)
    huellas.append(huellaUsuario)
    codigos.append(random.randrange(1000,9999))

def mostrar(numPersonas):
  print("Modulo de gestion")
  if (len(nombres) == 0 and len(huellas) == 0 and len(codigos) == 0):
    print("No existen registros")
  else: 
    for i in range(numPersonas):
      print("--------------------------")
      print(f'Mostrar los datos de la persona {i +1}')
      print("Nombre: ", nombres[i])
      print("Huella: ", huellas[i])
      print("Codigo: ", codigos[i])


def main():
  numPersonas = 0
  opcion = menu_opciones()
  while opcion != 4:
    if opcion == 1:
      numPersonas = int(input("Ingrese el numero de personas a registrar: "))
      while numPersonas >= 20 or numPersonas <= 0: #mientras no se cumpla se hara el while
        print("No puedes registrar numeros mayores a 20 ni negativos")
        numPersonas = int(input("Ingrese nuevamente numero de personas a registrar: "))
      registrar(numPersonas)
      opcion = menu_opciones()
    if opcion == 2:
      mostrar(numPersonas)
      opcion = menu_opciones() #pilas esto en funciones
    if opcion == 3:
      buscarUsuario()
      opcion = menu_opciones() #pilas esto en funciones
    if opcion >= 5:
      print("Opcion invalida ingrese nuevamente")
      opcion = menu_opciones() #pilas esto en funciones
print("Gracias vuelva pronto")

main()