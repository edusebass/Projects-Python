import random

datosBiometricos = [[],[],[]]
numPersonas = 0

def menuPrincipal():
  print("-----------------Sistema biometrico-----------------")
  print("-------------------Menu-----------------------------")
  print("¿Que accion desea realizar?")
  print("* 1)Login")
  print("* 2)Registro de usuarios")
  print("* 3)Salir del sistema")
  opcion = int(input("Ingrese la opcion: "))
  return opcion

def menuSecundario():
  print("\n ¿Que acción desea realizar?: ")
  print(f'*  1) Ingresar usuarios')
  print(f'*  2) Mostrar usuarios')
  print(f'*  3) Salir al menú principal')
  tipoAccion = int(input("Ingrese la opción: "))
  return tipoAccion

def logueo():
  print(f'-------- Bienvenido ----------')
  print()
  print("\t----Bienvenido - Módulos disponibles -------")
  print()
  print("¿Que acción desea realiar?: ")
  print(f'*  3) Cerrar sesión')
  tipo = int(input("Ingrese la opción: "))
  return tipo
def casos():
  opcion = menuPrincipal()
  while opcion != 3:
    if opcion == 1:
      if len(datosBiometricos[0]) == 0:
        print("\nNo existen usuarios. Registrese")
        opcion = menuPrincipal()
      else:
        user = int(input("Ingrese el rostro de la persona"))
        if user in datosBiometricos[1]:
          opcion = logueo()
        else:
          print("No existe el usuario, vuelva a intentarlo")
          opcion = menuPrincipal()
    if opcion == 2:
      tipoAccion = menuSecundario()
      while tipoAccion != 3:
        if tipoAccion == 1:
          numPersonas = int(input("\nIngrese el numero de personas a registrar: "))
          for i in range(numPersonas):
            print(f'Ingrese los datos de la persona {i +1}')
            nombreUsuario = input("Nombre de la persona: ")
            huellaUsuario = input("Huella de la persona: ")
            datosBiometricos[0].append(nombreUsuario)
            datosBiometricos[1].append(huellaUsuario)
            datosBiometricos[2].append(random.randrange(10000, 99999))
          print("\nPersona agregada!!!!!!!!!!!")
        tipoAccion = menuSecundario()
        if tipoAccion == 2:
          for i in range(numPersonas):
            print("-------------------------------------")
            print("Mostrando los datos de la persona", i + 1)
            print("* Nombre:", datosBiometricos[0][i])
            print("* Huella dactilar:", datosBiometricos[1][i])
            print("* Código de acceso: ", datosBiometricos[2][i])
            print("-------------------------------------")
          tipoAccion = menuSecundario()
      tipo = menuPrincipal()
  print("Muchas gracias")

def main():
  casos()

main()
