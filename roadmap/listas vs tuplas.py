# --------------------------- LISTAS VS TUPLAS ----------------------------
#lista
miPrimeraNovia = ["cariñosa"]
miPrimeraNovia[0] = "Toxica"
miPrimeraNovia[0] = "Chevere"
print(miPrimeraNovia[0]) 

#tupla
miSegundaNovia = ('cariñosa') #nunca se puede modificar

# --------------------------- TUPLAS ----------------------------

# Declarar una tupla vacía
nombre_de_la_tupla = ()

# Declarar una tupla con elementos
tuplaElementosUno = (1, 2, True, 'Hola', 5.8,'@','🍔')
tuplaElementosDos = 1, 2, True, 'Hola', 5.8,'@','🍔' #se puede poner sin parentesis pero no es recomendable

# Recorriendo los elementos con un for
tupla_Elementos = (23, True, 'Eduardo', 2.56, '@')
for i in tupla_Elementos:
    print(f'[{i}] ',end="")
print("\n\n")

#rrecorriendo tupla con while
indice = 0
while indice < len(tupla_Elementos):
  print(f'[{tupla_Elementos[indice]}] ',end="")
  indice += 1

print("\n-------------------------------------------------\n")

# Métodos disponibles para trabajar con tuplas 
# https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/tipo_tuplas.html


# Saber la longitud de una tupla
# print(len(tupla_Elementos))


# cuenta la cantidad de veces que aparece en la tupla
# print(tupla_Elementos.count('🍔'))


# Encontrar el índice de un elemento de la tupla
# print(tupla_Elementos.index('Hola amig@s'))

# Permite saber si un elemento está en una tupla.
# print(89 in tupla_Elementos)

# ---------------------- Conversión ---------------------------

# Tuplas a listas 
'''
listaElementos = list(tupla_Elementos)
print(type(listaElementos))
for i in listaElementos:
    print(f' {i} ',end="")

print("\n")
# Añadir un elemento al final de una lista
listaElementos.append('Quintales de arroz')
for i in listaElementos:
    print(f' {i} ',end="")
'''
  
  
# Listas a Tuplas
'''
listaFrutas = ["Cereza", "Pera","Uva","Kiwy"]
tuplaFrutas = tuple(listaFrutas)
print(type(tuplaFrutas))
for i in tuplaFrutas:
    print(f' {i}',end="")
'''
