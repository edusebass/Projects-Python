numero = int(input("Ingresa un numero: "))
sumatoria = 0

if (numero > 0) and (numero % 2 == 0):
  for i in range(0, numero+1):
    print (i)
    sumatoria += i
else:
  print("No se puede, el numero es negativo o es par")
print(f"La sumatoria es: {sumatoria}")