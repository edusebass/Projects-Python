#Para crear un conjunto por asignación debemos indicar sus elementos encerrados entre llaves y separados por coma.
conjunto1={1, 5, 10, 20}
print(conjunto1)
#Los elementos de un conjunto pueden ser de distinto tipo:
conjunto2={"juan", 20, 6.4, True}
print(conjunto2)
#Podemos definir elementos de un conjunto de tipo tupla pero no de tipo lista, diccionario o conjunto:
conjunto3={("juan", 33), ("ana", 44)}
print(conjunto3)
#podemos poner hacer lo siguiente
lenguajes={"C", "Pascal", "PHP", "Python"}
print(lenguajes) # {"C", "Pascal", "PHP", "Python"}
lenguajes.add("Ruby")
print(lenguajes) # {"C", "Pascal", "PHP", "Python, "Ruby"}
lenguajes.add("PHP")
print(lenguajes) # {"C", "Pascal", "PHP", "Python, "Ruby"}