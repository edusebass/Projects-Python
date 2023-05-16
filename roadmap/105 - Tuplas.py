# una tupla es inmutable no se puede modificar
tupla = (1, True, "Eduardo", "c", 1)  # siempre una tupla ira con parentesis()

"""
Recuerda que, dado que las tuplas son inmutables, los métodos como append(), 
remove(), insert(), etc., que se usan en las listas, no están disponibles para las tuplas.
"""
# Metodos
# Acceso a elementos de la tupla:
elemento = tupla[0]
print(elemento)

# Longitud de la tupla:
longitud = len(tupla)
print(longitud)

# Concatenación de tuplas:
tupla1 = (1, True, "Eduardo", "c")
tupla2 = (1, True, "Eduardo", "c")

nueva_tupla = tupla1 + tupla2
print(nueva_tupla)

# count(valor): Devuelve el número de veces que aparece un valor en la tupla.
vececs = tupla.count(1)
print(vececs)

# index(valor): Devuelve el índice de la primera aparición de un valor en la tupla
indice = tupla.index("Eduardo")
print(indice)

#### ejemplos
tupla3 = (1, 2, 3, 2)
tupla4 = (4, 5, 6)
nueva_tupla = tupla3 + tupla4  # Concatenación de tuplas
print(nueva_tupla)  # Resultado: (1, 2, 3, 2, 4, 5, 6)

repetida_tupla = tupla3 * 2  # Repetición de tupla1
print(repetida_tupla)  # Resultado: (1, 2, 3, 2, 1, 2, 3, 2)

contador = tupla3.count(2)  # Contar la cantidad de veces que aparece el valor 2
print(contador)  # Resultado: 2

indice = tupla3.index(3)  # Obtener el índice de la primera aparición del valor 3
print(indice)  # Resultado: 2
