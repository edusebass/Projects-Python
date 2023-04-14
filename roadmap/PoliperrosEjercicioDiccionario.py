from os import system
numPerros=0
datosPoliperros = {
  'nombre':[],
  'huellaDactilar':[],
  'foto':[],
}
def menu():
  print("------------ POLIPERROS -------------")
  print("\n\t\t *** Bienvenido(a) ***\n")
  print("¿Que acción desea realizar?")
  print("*  1) Registrar poliperros")
  print('*  2) Mostrar poliperros')
  print('*  3) Registrar foto del poliperro')
  print('*  4) Eliminar un poliperro')
  print('*  5) Salir del sistema')
  opcion = int(input("Ingrese la opción: "))
  return opcion
def menu_de_registrar():
  print("-------Borrar registros de poliperros------")
  print("* 1) Borrar un registro")
  print("* 2) Limpiar todos los registros")
  print("* 3) Regresar al menu")
  opcion = int(input("Ingrese la opcion: "))
  return opcion
def registrar(numPerros, datosPoliperros):
  for i in range(numPerros):
    nombre = str(input(f'Ingrese el nombre del poliPerro #{i + 1}: '))
    huella = input("Ingrese el codigo de la huella: ")
    datosPoliperros['nombre'].append(nombre)
    datosPoliperros['huellaDactilar'].append(huella)

def mostrarperro(numPerros, datosPoliperros):
  if len(datosPoliperros['nombre']) == 0:
    print ("Sin registros en el sistema")
  else:
    for i in range(len(datosPoliperros['nombre'])):
      print("-------------------------------------")
      print("Mostrando los datos del poliperro", i + 1)
      print("* Nombre:", datosPoliperros['nombre'][i])
      print("* Huella dactilar:", datosPoliperros['huellaDactilar'][i])
      if ("foto" in datosPoliperros['foto']):
        print("* Foto: ", datosPoliperros['foto'][i])
        print("-------------------------------------")
      else: 
         print("* Foto: --NO SE ENCUENTRAN REGISTROS DE FOTOS--")
        
def fotoperro(numPerros, datosPoliperros):
  if len(datosPoliperros['nombre']) == 0:
    print("Ingrese primero un perro")
  else:
    for i in range(numPerros):
      print(f'Ingrese la foto del poliPerro {i + 1}')
      print("El poliperro tiene foto?")
      respuesta = input("Ingrese 'si' o 'no': ")
      if respuesta == "si":
        datosfoto = input("Foto: ")
        datosPoliperros['foto'][i].append(datosfoto)
      else:
        print("--NO SE AGREGO FOTO--")
    datosPoliperros.update(datosPoliperros)
# def eliminarperro(datosPoliperros, numPerros):
#   opcion = menu_de_registrar()
#   while opcion != 3:
#     if opcion == 1:
#       if len(datosPoliperros['nombre']) == 0:
#         print("No existen registros")
#     opcion = menu_de_registrar()
#     if opcion == 2:
#       datosPoliperros.clear()
#       datosBorrados = {
#         'nombre':[],
#         'huella_dactilar':[],
#         'foto':[]
#       }
#       datosPoliperros.update(datosBorrados)
#       print("DATOS BORRADOS CORRECTAMENTE")
#     opcion = menu_de_registrar()
#   opcion = menu()
def main():
  numPerros=0
  datosPoliperros = {
    'nombre':[],
    'huellaDactilar':[],
    'foto':[]
  }
  opcion = menu()
  while opcion != 5:
    if opcion == 1:
      system('clear')
      numPerros = int(input("Ingrese el numero de poliPerros a registrar #: "))
      registrar(numPerros, datosPoliperros)
      opcion = menu()
    if opcion == 2:
      system('clear')
      mostrarperro(numPerros, datosPoliperros)
      opcion = menu()
    if opcion == 3:
      system('clear')
      fotoperro(numPerros, datosPoliperros)
      opcion = menu()
      
    if opcion == 4:
      system('clear')
      # eliminarperro(numPerros, datosPoliperros)
      opcion = menu()
      
main()
