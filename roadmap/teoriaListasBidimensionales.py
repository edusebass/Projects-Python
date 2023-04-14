'''
  La matrices no son una estructura propia de Python. 
  
  Simplemente, una matriz es una lista de listas que nosotros 
  interpretamos desde el punto de vista matemático. 
  
  Es decir,la estructura m = [[1,2],[3,4]] nosotros la interpretamos 
  como la matriz 2x2 cuya primera fila es (1,2) y cuya segunda fila es (3,4).
'''
'''
  En Python, las matrices se representan mediante el tipo de datos de lista.

  Ejemplo de una matriz de 3x3

  M1 = [[8, 14, -6], [12,7,4], [-11,3,21]]
'''
# --------------------------- MATRICES ----------------------------
mi_tabla = [['Byron', 'Edu', 'rachel', 'ninann'],
            ['Byron', 'selena', 'monica', True]]

#obtener elementos
'''print(mi_tabla[0][0])'''

#recorrer una lista con bucle
trailerElementos = [['Byron', 'Anita',True,'@'], [21, 32,False,'🍔']]

#recorrer un elementos con for

for f in range(len(trailerElementos)): #travel filas
  for c in range(len(trailerElementos[f])): # get columnas
    print(f'{trailerElementos[f][c]} ', end = "")
  print("\n")

#recorriendo elementos con un while
f = 0
c = 0

while f < len(trailerElementos):
  c = 0
  while c < len(trailerElementos[f]):
    
    print(f'{trailerElementos[f][c]} ', end = "")
    c += 1
  print("\n")
  f += 1