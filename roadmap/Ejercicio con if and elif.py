#Ejericio 5 LABORATORIO 03
'''
En la Escuela Politécnica Nacional en el Departamento de Bienestar Estudiantil, se
requiere de un programa que permita realizar el cálculo del IMC de cualquier persona. En
ese sentido, realice un algoritmo, represéntelo mediante un diagrama de flujo,
pseudocódigo y el programa respectivo para determinar el IMC en base a la siguiente
formula. 
'''




print("A continuacion se calculara su indice de IMC\n")
estatura = float(input("Ingrese su estatura: "))
peso = float(input("Ingrese su peso en Kg: "))

imc = peso / (estatura * estatura)
print("Su indice de IMC es: ", imc)

if (imc < 18.5) :
  print("Por lo tanto usted tiene: Bajo de peso")
elif (imc > 18.5 and imc < 24.9):
  print("Por lo tanto usted esta: Normal")
elif (imc > 25 and imc < 29.9):
  print("Por lo tanto usted tiene: Sobrepeso")
elif (imc > 30 and imc < 34.9):
  print("Por lo tanto usted tiene: Obesidad I")
elif (imc > 35 and imc < 39.9):
  print("Por lo tanto usted tiene: Obesidad II")
elif (imc < 40):
  print("Por lo tanto usted tiene: Obesidad III")
