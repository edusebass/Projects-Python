#FUNCION TIPO VOID SIN RETURN NI PARAMETROS
def holamundo():
  print("Hola mundo")

#DECLARAR Y DESARROLAR CON PARAMETROS
def suma(num1,num2):
  resultado = num1 + num2
  return resultado

def molino(tipo):
  print(f"{tipo} molido(a)")

def numeroReversa(numero):
  while numero > 0:
    print(numero)
    numero -= 1

def procesarNumero(num):
  if num == 4:
    return num * 4
  elif num == 3:
    return num * 3
  elif num == 5:
    return num * 5
  else:
    return num
    
#INVOCAR LA FUNCION
holamundo()
#-----
resultadoDos = suma(4,6)
print(resultadoDos)         #dos formas para imprimir el return

print(suma(4,6))
#----------
molino("molida")

#---------
a = int(input("= "))
numeroReversa(a)
numeroReversa(int(input("= ")))

#-----
print(f"El resutlado es {procesarNumero(3)}")

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

varibleUno = 2 
variableDos = 10

def funcionDemo():
  print("---->", variableUno)
  

  variableDos = 20
  printprint("---->", variableDos)

funcionDemo(2
           )


def menu():
  print("-----------")
  print("\tMenu")
  print("\t 1.- Juego del Pacman")
  print("\t 2.- Area del trapecio")
  print("\t 3.- Transformar temperaturas")
  print("\t 4.- Salir")
  opcion = int(input("Ingrese opcion: "))
  return opcion

def login():
  user = input("Ingrese su nombre: ")
  password = int(input("Ingrese su password: "))

  if user == "edu" and password == 123:
    return True
  else:
    print("Las credenciales son incorrectas")
    return False

def pacman(nombreJugador, nivelJuego):
  poderPacman = 500
  vidasJugador = 3
  if nivelJuego == 2 and vidasJugador == 3:
    poderPacman += 100
    print("Felicitaciones")
    print(f"El nuevo poder es de {poderPacman}")
  elif nivelJuego == 3 and vidasJugador == 3:
    poderPacman += 300
    print("Felicitaciones")
    print(f"El nuevo poder es de {poderPacman}")
  elif nivelJuego == 4 and vidasJugador == 4:
    poderPacman += 300
    print("Felicitaciones")
    print(f"El nuevo poder es de {poderPacman}")
  else:
    print(nombreJugador)
    print(f"Su poder es {poderPacman}")


def temp(sistema):
  grados = 0
  fare = 0
  if sistema == 1:
    grados = int(input("Ingrese grados: "))
    fare = (grados * 1.8) + 32
    print(fare)
  elif sistema == 2:
    fare = int(input("Ingrese farenheit: "))
    grados = (fare - 32) / 1.8
    print(grados)
  
def main():
  if login():
    opciMenu = menu()
    while opciMenu != 4:
      if opciMenu == 1:
        nombre = input("Ingresa tu nombre: ")
        nivel = int(input("Ingresa tu nivel de juego: "))
        pacman(nombre, nivel)
        opciMenu = menu()
      elif opciMenu == 2:
        print("Caso 2")
        opciMenu = menu()
      elif opciMenu == 3:
        print("Transformar temperaturas")
        sistema = int(input("1)C a F \n2)F a C\nIngrese la opcion: "))
        temp(sistema)
        opciMenu = menu()
    
    print("Muchas gracias")

main()