import os
from os import system
# DECLARA TUS VARIABLES 👻
# SOLICITA DATOS AL USUARIO 🤠
print("Cargando datos...")
print("Bienvenido a Facebook")
print("Si tiene una cuenta ingrese si")
print("Si no tiene una cuenta ingrese no")
login=input("Ingrese la palabra: ")

if login=="si":
  system("clear")
  user=input("Ingrese su nombre de usuario: ")
  password=input("Ingrese su contraseña: ")
  if (user=="byron") and (password=="123"):
    system("clear")
    print("Bienvenido ", user)
    print("Revisa tus últimos estados")
    print("* MOMOS EPN")
    print("* ESFOT EPN")
    print("* POLICRUSH EPN")
  else:
    print("Usuario y contraseña incorrectos ")
else:
  system("clear")
  print("Para crear una nueva cuenta, ingresa los siguientes datos")
  correoElectronico=input("Ingresa tu correo electrónico: ")
  user=input("Ingresa tu nombre de usuario: ")
  password=input("Ingresa una contraseña: ")
  print("Excelente, ya puedes iniciar sesión")
#REALIZA EL PROCEDIMIENTO 🔎
# IMPRIME LOS RESULTADOS 💡


# GENIAL ERES UN EXCELENTE PROGRAMADOR(A)⭐