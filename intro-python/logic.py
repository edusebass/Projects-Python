#multiplicar dos numeros sin usar el simbolo de multiplicacion
from ast import Try
from mimetypes import init


a = 4
b = 8

resultado = 0

for x in range(b):
    resultado = resultado + a

print(resultado)

#ingresar nombre y apellido e imprimirlo al reves

nombre = 'Eduardo'
apellido = 'Almachi'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])

# write a function that finds the less element of a list

list = [1,2,3,4,5,43,234,2343234,-13,-23,-34]

less = 'init'

for x in list:
    if less == 'init':
        less = x
    else:
        less = x if x < less else less

print('less:', less)   

#write a function that returns the volumen of a sphere for his radio

def calculateVolume(r):
    return 4 / 3 * 3.14 * r ** 3

result = calculateVolume(8)
print(result)

# write a function that indicates if the usuario is adult

def esMayor(usuario):
    return usuario.age > 17

class Usuario:
    def __init__(self, age):
        self.age = age

usuario = Usuario(18)
usuario2 = Usuario(15)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)

# write a function that indicates if a number is odd or pair

def isPair(n):
    return n % 2 == 0

resultado = isPair(10)
print(resultado)

# write a function that indicates how many vocals have a word

palabra = 'EduardoAlmachi'
vocales = 0

for x in palabra:
    y = x.lower()    #so that it takes into account the capital letters too
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

#print(vocales)

# write a aplication that recieve a infinite amount of numbers until 
# enough is said, then it returns the sum of the numbers entered

list = []
#print('Write the numbers and for exit writes "stop"')
#while True:
#    valor = input('Enter a value: ')
#    if valor == 'stop':
#       break
#   else:
#       try:
#            valor = int(valor)    # (int) works only to collect numbers
#            list.append(valor)
#        except:
#            print('invalid date')
#            exit()

#result = 0
#for x in list:
#    result += x

#print(result)

# write a function that recieve name and surname and that add to a file

def addNameFile(name, surname):
    c = open('completname.txt', 'a')
    c.write(name + ' ' + surname + '\n')
    c.close()

addNameFile('Eduardo', 'Almachi')

