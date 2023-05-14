def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        print("No se pueden multiplicar las matrices. Las dimensiones no son válidas.")
        return None

    matriz_resultante = [[0] * columnas_matriz2 for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(columnas_matriz1):
                matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz_resultante


# Definir la matriz 1 (2x3)
matriz1 = [[1, 2, 3], [4, 5, 6]]

# Obtener los elementos de la matriz 2 (3x2) del usuario
matriz2 = []
print("Ingrese los elementos de la matriz 2 (3x2):")
for _ in range(3):
    fila = [
        int(elemento)
        for elemento in input(
            "Ingrese una fila de 2 números separados por espacios: "
        ).split()
    ]
    matriz2.append(fila)

# Multiplicar las matrices
matriz_resultante = multiplicar_matrices(matriz1, matriz2)

# Imprimir la matriz resultante
if matriz_resultante:
    print("La matriz resultante es:")
    for fila in matriz_resultante:
        print(" ".join(str(elemento) for elemento in fila))
