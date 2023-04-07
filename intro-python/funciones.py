# FUNCIONES


def mifuncion():
    print("mi primera funcion")

#mifuncion()


def imprimedato(argumentoUno):
    print("mi argumento es", argumentoUno)

imprimedato("parametro 1")


def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
