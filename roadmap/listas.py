''#------------------LISTAS----------------
#creacion de una lista
nombre_de_la_list = [1, 2, True, 'Hola', 5.8, '@']
otra_lista = list([4, 9, False, 'Hola amigos', ':)'])

#la primera posicion siempre es 0
#la ultima posicion  de la lista es siempre (tamaño de la lista - 1)
#si accedes a un indice que no existe el programa fallara
tren_de_elementos = [4,   9,  False, 'Hola amig@s','🍔',8.9]
#                   [0]--[1]---[2]--------[3]-------[4]--[5]

#impresion de un arreglo
print(tren_de_elementos[0])
print(tren_de_elementos[1])
print(tren_de_elementos[2])
print(tren_de_elementos[3])
print(tren_de_elementos[4])
print(tren_de_elementos[5])
print(tren_de_elementos[5])

#reasignacion de valor 
tren_de_elementos[5] = True
print(tren_de_elementos[5])

#si se imprime el indice 10 fallara puesto que no lo hay
print("----------")

#recorrer los elementos con un bucle for
for i in tren_de_elementos:
    print(f'[{i}]', end = " ") #el end se utiliza para que se imprima como tren seguido
    
print("----------")

#recorrer los elementos con un bucle while
indice = 0
while indice < len(tren_de_elementos):  #-------------> len se utiliza metodo es para saber la longitud del arreglo
    print(f'[{i}]', end = " ")
    indice += 1 #ese algo


print("----------")
#-----------------------UNIR LISTAS-----------
trenFrutas = ['Cereza', 'Pera', 'Uva', 'Kiwi']
trenVerduras = ['Brocoli', 'Zanahoria', 'Espinaca']

trenAlimentos = trenFrutas + trenVerduras
for i in trenAlimentos:
    print(f'[{i}]', end = "")

print("------------------------")    
print("METODOS")    
# #---------------------------METODOS-----------------------------------
tren_de_elementos = [4,   9,  False, 'Hola amig@s','🍔',8.9]

# #saber la longitud de elementos
print(len(tren_de_elementos))


# #añadir un elemento a la final de una lista
tren_de_elementos.append('Quintal de arroz')
for i in tren_de_elementos:
    print(f'[{i}]', end = " ")


# #añador un elemento x en la lista a traves de indice i
tren_de_elementos.insert(2, 'Cajas de Bananas') #primera condicion indice de posicion , segundo nombre de lo que quieres
for i in tren_de_elementos:
    print(f'[{i}]', end = " ")
    

# # Devuelve el último elemento de la lista y lo borra de la misma
# # Se puede pasar el índice también
tren_de_elementos.pop()
for i in tren_de_elementos:
    print(f'[{i}]', end = " ")

   
# # Recibe como argumento un elemento y borra su primera aparición en la lista.
tren_de_elementos.remove(9)
for i in tren_de_elementos:
    print(f'[{i}]', end = " ")


# # Eliminar todos los elementos de una lista
tren_de_elementos.clear()


# Encontrar el índice de un elemento de la lista
print(tren_de_elementos.index('Hola amig@s'))


#Invertir el orden de la lista
tren_de_elementos.reverse()
for i in tren_de_elementos:
    print(f'[{i}]', end = " ", )
    
    
#Ordenar lista
versionesJuego = [[4, 2.5, 5, 3.6, 2.1, 6]]
versionesJuego.sort()
for i in versionesJuego:
    print(f'[{i}]', end = " ")

# Contar cuántos elementos de la lista tienen un valor dado
print(versionesJuego.count(9))

