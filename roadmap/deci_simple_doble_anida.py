# ESTRUCTURA DE DECISIÓN SIMPLE 
#dec_simple_doble_anida

'''
if (condición a evaluar): # Por ejemplo X >= 10
    # Bloque de instrucciones si se cumple la condición....
    # Solo se ejecutará si la condición es verdadera

# Bloque de Instrucciones restante del programa....
# Se ejecuta siempre, pues está fuera de la condición

'''
'''
❗️ IMPORTANTE
  El cuerpo del bloque está indicado con un sangrado mayor. 
  Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
'''

x = 17
if x < 20:
  print(x,'es menor que 20')

# siempre luego de lacondicion del if va con dos puntos(:)
y = 23
if y == 23:
  print(y, "es igual a 23")


# ===============================================================================================
# ESTRUCTURA DE DECISIÓN DOBLE

'''
if (condición a evaluar): # Por ejemplo Z <= 50 
    # Bloque de instrucciones SI se cumple la condición....
    # Solo se ejecutará si la condición es verdadera
else:
    # Bloque de instrucciones si NO se cumple la condición....
    # Solo se ejecutará si la condición es falsa

# Bloque de Instrucciones restante del programa....
# Se ejecuta siempre, pues está fuera del if else
'''


x = 10
y = 60
if (y != 0):
    print("La división es: ", x / y )
else:
    print("No se puede dividir",x,"entre",y)

print("Se ejecuta lo que esta fuera del if-else")
print("==============================================================================")
print("\n")

  #EJERCICIO 6 (LABORATORIO)

nombrecliente = input("Ingrese su nombre: ")
totalcompra = float(input("Ingres el precio final: "))

if totalcompra >= 500:
  descuentoaplicado = (totalcompra * 70) / 100
  print("El valor a pagar con el descuento es: ", descuentoaplicado)
else:
  print("Su compra no supera los 500 dolares, por ende el valor a pagar es: ", totalcompra)

#===============================================================================================

                          #   ESTRUCTURA DE DECISIÓN ANIDADA

'''
Los condicionales, permiten escribir código en su interior y en realidad, nada impide incluso al interior de un condicional, poner otros (u otros) condicionales. 

A eso se le llama condiciones anidadas, pues es una estructura condicional dentro de otra. De hecho, puedes anidar cuantos condicionales requieras.

'''

'''
if cond1:
    bloque cond1 (sentencias que se ejecutan si se evalúa la cond1 a True)
elif cond2:
    bloque cond2 (sentencias que se ejecutan si cond1 es False pero cond2 es True)
...
else:
    bloque else (sentencias si todas las condiciones se evalúan a False)
'''

x = 19999
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
elif x == 0:
    print(f'{x} es igual que 0')
elif x != 0:
    print(f'{x} es diferente que 0')
else:
    print('x es 0')


x = 28
if x < 0:
    print(f'{x} es menor que 0')
else:
    if x > 0:
        print(f'{x} es mayor que 0')
    else:
        print('x es 0')


      #Ejercicio

if (1<2):
  if(2>3):
    print("accion a")
  else:
    print("accion b")


if(condicion externa):
  if(condicion interna1):
    print("accion1")
  else:
    print"accion2")
    
else:
  if(condicioninterna2)
    print("accion3")
  else:
    print("accion4")



