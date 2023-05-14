#   LISTAS
# siempre las listas van a estar con corchetes cuadrados []
lista = [1, "Eduardo", True, 2.30, "c"]
print(lista)

# posiciones       0      1        2     3    4
listaposiciones = [1, "Eduardo", True, 2.30, "c"]


#      metodos

"""
append(elemento): Agrega un elemento al final de la lista.
"""
lista2 = [1, 2, 3]
lista2.append(True)
print("lista2: ", lista2)

"""
extend(iterable): Extiende la lista agregando los elementos de otro iterable, como otra lista o una tupla.
"""
lista3 = [4, 5, 6]
lista4 = [7, 8, 9]
lista3.extend(lista4)
print("lista 3: ", lista3)
"""
insert(posición, elemento): Inserta un elemento en una posición específica de la lista. 
#que no reemplaza al elemento si no que sustituye su posicion
"""
# posicion    0       1     2
lista5 = ["Eduardo", True, "c"]
lista5.insert(0, "Sebastian")  # ["Sebastian", "Eduardo", True, "c"]
print("lista 5: ", lista5)

"""
remove(elemento): Elimina la primera aparición del elemento especificado en la lista.
"""
lista6 = [2, 3, 3, 2]
lista6.remove(2)
print("lista 6: ", lista6)
"""
pop([posición]): Elimina y devuelve el elemento en la posición especificada. Si no se proporciona una posición, se elimina y devuelve el último elemento de la lista.
"""
lista7 = [1, True, 3]
elemento = lista7.pop(1)
print(elemento)  # Resultado: True
print("lista 7: ", lista7)  # Resultado: [1, 3]
"""
index(elemento): Devuelve el índice de la primera aparición del elemento especificado en la lista.
"""
lista8 = [1, "EDUARDO", True, "Selena"]
índice = lista8.index("Selena")
print("Selena esta en la posicion: ", índice)

"""
count(elemento): Devuelve el número de veces que aparece el elemento en la lista.
"""
lista9 = [True, False, True, "☝️", True, False, True, "☝️"]
ocurrencias = lista9.count(True)
print("true se repite: ", ocurrencias)
"""
sort(): Ordena los elementos de la lista en orden ascendente.
"""
lista10 = [3, 1, 4, 2]
lista10.sort()
print("lista10: ", lista10)  # Resultado: [1, 2, 3, 4]
"""
reverse(): Invierte el orden de los elementos en la lista.
"""
lista11 = [1, 2, 3]
lista11.reverse()
print("lista11: ", lista11)  # Resultado: [3, 2, 1]
"""
clear(): Elimina todos los elementos de la lista, dejándola vacía.
"""
lista12 = [1, 2, 3]
lista12.clear()
print("lista eliminada", lista12)  # Resultado: []
