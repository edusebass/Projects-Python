def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


# Ejemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento_buscado = 11

indice = busqueda_binaria(numeros, elemento_buscado)

if indice != -1:
    print("El elemento", elemento_buscado, 
          "se encuentra en el índice", indice)
else:
    print("El elemento", elemento_buscado,
          "no se encuentra en la lista")
