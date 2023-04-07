from platform import java_ver


def miFuncion():
    print('Mi primera funcion')

#miFuncion()


def imprimeDato(nombre, apellido):
    print('El nombre completo es:', nombre, apellido)

#imprimeDato('Eduardo', 'Almachi')


def imprimeDato1(*nombre): #el asterisco se utiliza para  hacer lo de abajo 14
    print('El nombre completo es:', nombre[0]) #esto es para acceder a uno en especifico

#imprimeDato1('Eduardo', 'Almachi')


def nombreCompleto(apellido, nombre):
    print(nombre, apellido,)

#nombreCompleto(nombre='Eduardo', apellido='Almachi')      #esto se ultiliza cuando no tenemos el orden concreto 19


def nombreCompleto2(**kwargs):     #kwargs sirve para acceder a los argumentos utilizando la sintaxis de diccionario
    print(kwargs['nombre'],kwargs['apellido'])

#nombreCompleto(nombre='Eduardo', apellido='Almachi')


def mifuncion2(argumento= 'Eduardo'):  #se utiliza para añadir un argumento automatico 34
    print(argumento)

#mifuncion2('rita')          
#mifuncion2()                   #en este caso se imprimira rita pero luego Eduardo por 30


def mifuncionlista(lista):
    for el in lista:
        print(el)

#mifuncionlista(['Eduardo', 'Sebastian'])  #esto funciona para que en vez de imprimirse recto sea arriba para abajo


def concatenarnombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenarnombres(['Eduardo', 'Sebastian'])
#print(nombres)                                             #otra manera de imprimir funciones


def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)