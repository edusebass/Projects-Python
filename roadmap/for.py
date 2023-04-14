# # https://www.mclibre.org/consultar/python/lecciones/python-for.html#Paso019
#                              FOR

'''
Para entender al cien por cien los bucles for y como Python fue diseñado como lenguaje de programación, es muy importante entender los conceptos de iterables e iteradores.

'''


'''
  * Los iterables
      Son aquellos objetos que como su nombre indica pueden ser iterados
      En Python los tipos principales list, tuple, dict, set o string entre otros, son 
      iterables, por lo que podrán ser usados en el bucle for.

  * Los iteradores 
      Son objetos que hacen referencia a un elemento, y que tienen un método next que 
      permite hacer referencia al siguiente.
      Un iterador recorre los elementos de un iterable solo hacia delante.
'''


print("----------------")
for i in [0, 1, 2]:
    print(i,"Hola amig@s")
print("----------------")

# print("\n\n\n")





print("----------------")
for i in "parang":
    print(i)
print("----------------")

# print("\n\n\n")





print("----------------")
for i in range(1,6): # [1,2,3,4,5]
    print(i,"Hola amig@s")
print("----------------")

# print("\n\n\n")


for i in range (0,10,2):
  print(i)

# print("\n\n\n")




print("----------------")
dato=int(input("Ingrese el valor: "))
for i in [1, 3, 5, 7, 9]:
  x = i**dato - (i-1)*(i+1)
  print(x)
print("----------------")


print("\n\n\n")


print("----------------")
trenNumeros = [2, 4, 5, 7, 8, 9, 3, 4]
for e in trenNumeros:
    print("----------->",e)
    if e % 2 == 0:
      print(e)
print("----------------")



# print("\n\n\n")


# print("----------------")
# for i in ["Alba", "Benito", 27]:
#     print(f"Hola. Ahora i vale {i}")
# print("----------------")





# print("\n\n\n")


print("----------------")
i = 10
print(f"El bucle no ha comenzado. Ahora i vale {i}")
for i in [0, 1, 2, 3, 4]:
    print(f"{i} * {i} = {i ** 2}")
print(f"El bucle ha terminado. Ahora i vale {i}")
print("----------------")