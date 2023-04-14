datos = {
  'nombre':[],
  'apellido':[],
  'telefono':[],
  'domicilio':[],
  'codigo':[]
}
redatos = 0
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
telefono = input("Ingrese el telefono: ")
domicilio = input("Ingrese el domicilio: ")
codigo = input("Ingrese el codigo: ")

print(len(datos))

datos['nombre'].append(nombre)
datos['apellido'].append(apellido)
datos['telefono'].append(telefono)
datos['domicilio'].append(domicilio)
datos['codigo'].append(codigo)

redatos += 1
len(datos) == redatos


for i in range(redatos):
  print(datos['nombre'][i])
  print(datos['apellido'][i])
  print(datos['telefono'][i])
  print(datos['domicilio'][i])
  print(datos['codigo'][i])