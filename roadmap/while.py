
# https://www.mclibre.org/consultar/python/lecciones/python-while.html

'''
  El uso del while nos permite ejecutar una sección de código repetidas veces.
  
  El código se ejecutará mientras una condición determinada se cumpla. Por otra parte, cuando se deje de cumplir 
  la condición se saldrá del bucle y se continuará la ejecución normal. 

  Llamaremos iteración a una ejecución completa del bloque de código.

'''

'''
  Por lo tanto el while tiene dos partes:
    * La condición 
        Que se tiene que cumplir para que se ejecute el código.

    * El bloque de código 
        Que se ejecutará mientras la condición se cumpla.
'''

'''
  Ten cuidado ya que un mal uso del while puede dar lugar a bucles infinitos y problemas.
'''
 #BUCLE INFINITO                # while(True):
                                #   print("Bucle infinito")
'''
i = 1
while i<=3:
  print(i)
  i+=1 #siempre debe haber esto ese ALGO PARA QUE NO SE HAGA INFINITO
'''
'''
i = 1
while i <= 50:
  print(i)
  i = 3 * i + 1 #siempre debe haber esto ese ALGO PARA QUE NO SE HAGA INFINITO
'''

'''
password = int(input("Ingresa un password: "))  
while password != 123:
  print("Password incorrecto")
  password = int(input("Ingresa un password: ")) #debe haber ese algo para que no se haga bucle
print("Bienvenido al sistema")
'''
5

# reiniciarprograma = str("si")
# while reiniciarprograma == "si":
#   print("Realizar pedido....")
#   reiniciarprograma = str(input("Desea realizar un pedido? "))
# print("Muchas gracias por su compra")


from os import system

puntoInicial = int(input("Ingrese el punto inicial: "))

puntoFinal = int(input("Ingrese el punto final: "))

sumatoria = 0

while puntoInicial > puntoFinal:
  system("clear")
  print("-----------ERROR-----------")
  print("El punto inicial debe ser menor que el final")
  puntoInicial = int(input("Ingrese el punto inicial: "))
  puntoFinal = int(input("Ingrese el punto final: "))

system("clear")
while puntoInicial <= puntoFinal:
  sumatoria += puntoInicial
  puntoInicial += 1

print(f'La sumatoria es: {sumatoria}')



