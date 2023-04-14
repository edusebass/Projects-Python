'''
  Un acumulador 
    Es una variable que se utiliza para sumar valores. 
    Al igual que el contador, se utiliza normalmente dentro de un ciclo 
    pero cambiamos su valor sumándole una variable, es decir, no siempre 
    se le suma la misma cantidad.

'''


'''
  Por ejemplo
  Una cuenta de ahorros puede representarse en un algoritmo mediante un acumulador, pues 
  el ahorrista no siempre podrá ahorrar una cantidad fija en la cuenta, 
  un día deposita 100, otro día retira 30, otro deposita 5 y así sucesivamente.
'''


cuentaBancaria = 100

accion = "retiro"

if accion == "deposito":
  monto = int(input("Ingrese el monto a depositar: "))
  cuentaBancaria  = cuentaBancaria + monto
else:
  monto = int(input("Ingrese el monto a retirar: "))
  cuentaBancaria = cuentaBancaria - monto

print("El saldo de su cuenta bancaria es: ", cuentaBancaria)
