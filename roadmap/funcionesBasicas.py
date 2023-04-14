def menu():
  print("-----------")
  print("\tMenu")
  print("\t 1.- Juego del Pacman")
  print("\t 2.- Area del trapecio")
  print("\t 3.- Tarea Desafio")
  print("\t 4.- Salir")
  opcion = int(input("Ingrese opcion: "))
  return opcion

def login():
  user = input("Ingrese su nombre: ")
  password = int(input("Ingrese su password: "))

  if user == "Byron" and password == 123:
    return True
  else:
    print("Las credenciales son incorrectas")
    return False