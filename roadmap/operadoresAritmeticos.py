                            # 📗 Operadores Aritméticos
#ope_arit_asig_rela_bole
'''
Los operadores aritméticos son los más comunes que nos podemos encontrar, y nos permiten realizar operaciones aritméticas sencillas, como pueden ser la suma, resta o exponente.
'''

x = 10; y = 3
print("Operadores aritméticos")
print("x + y =>", x+y)   #13
print("x - y =>", x-y)   #7
print("x * y =>", x*y)   #30
print("x / y =>", x/y)   #3.3333333333333335
print("x % y =>", x%y)   #1
print("x ** y =>", x**y) #1000
print("x // y =>", x//y) #3


'''
😉 Importante
El orden de prioridad sería el siguiente para los operadores aritméticos, siendo el primero el de mayor prioridad:

  () Paréntesis
  ** Exponente
  -x Negación
  * / // Multiplicación, División, Cociente, Módulo
  + - Suma, Resta
'''
print(10*(5+3)) # Con paréntesis se realiza primero la suma
print(3*3+2/5+5%4) # Primero se multiplica y divide, después se suma



# 📗 Operadores de asignación
'''
Los operadores de asignación nos permiten realizar una operación y almacenar su resultado en la variable inicial. 
'''
a=7; b=2
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5
x=a; x%=b;  print("x%=", x)  # 1
x=a; x//=b; print("x//=", x) # 3
x=a; x**=b; print("x**=", x) # 49

# 📗 Operadores Relacionales
#operadoresrelacionales
'''
Los operadores relacionales nos permiten saber la relación existente entre dos variables
'''

x=2; y=3
print("Operadores Relacionales")
print("x==y =", x==y) # False
print("x!=y =", x!=y) # True
print("x>y  =", x>y)  # False
print("x<y  =", x<y)  # True
print("x>=y =", x>=y) # False
print("x<=y =", x<=y) # True


# 📗 Operadores Lógicos o booleanos

'''
Los operadores lógicos nos permiten trabajar con valores de tipo booleano. 

Un valor booleano o bool es un tipo que solo puede tomar valores True o False. 

Por lo tanto, estos operadores nos permiten realizar diferentes operaciones con estos tipos, y su resultado será otro booleano.

'''


print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False


print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False


print(not 0) # True
print(not 1) # False



datoUno = 8
datoDos = 3
print(datoUno>datoDos and datoDos==datoUno or datoDos!=datoUno)