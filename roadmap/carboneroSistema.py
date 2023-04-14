print("*******BIENVENIDO AL CARBONERO**********\n")

print("Ingrese los datos para la factura electronica")
print("Ingrese su nombre: ")
nombre = (input())

print("Ingrese su numero de cedula: ")
cedula = int (input())

print("Ingrese el numero de hamburguesas a adquirir: ")
num_ham = int(input())

print ("Ingrese que tipo de hamburguesa desea: ")
print ("1) Hamburguesa sencilla\n")
print ("2) Hamburguesa doble\n")
print ("3) Hamburguesa triple\n")
tipo_ham = int(input())

if tipo_ham == 1:
  a = 1.50
  print("\n")
  print("Ingrese su forma de pago: ")
  print("1) Tarjeta de credito ")
  print("2) Efectivo: ")
  pago = int(input())
  
  total = a * num_ham
  
  if pago == 1:
    total = a * (num_ham) + ((a*num_ham)*5/100)
    print ("*****************FACTURA******************")
    print("DATOS")
    print("Cedula: ", cedula)
    print("Nombre: ", nombre)
    print("Listo,",nombre," por las ",num_ham, "hamburguesas, el precio final con tarjeta es: ", total)
    print("GRACIAS POR SU COMPRA")
  else:
    print ("*****************FACTURA******************")
    print("DATOS")
    print("Cedula: ", cedula)
    print("Nombre: ", nombre)
    print("Listo, por las ",num_ham, "hamburguesas, el precio final en efectivo es: ", total)
    print("GRACIAS POR SU COMPRA")
  
elif tipo_ham == 2:
  a = 2.50
  
  print("\n")
  print("Ingrese su forma de pago: ")
  print("1) Tarjeta de credito ")
  print("2) Efectivo: ")
  pago = int(input())
  
  total = a * num_ham
  
  if pago == 1:
    total = a * (num_ham) + ((a*num_ham)*5/100)
    print ("*****************FACTURA******************")
    print("DATOS")
    print("Cedula: ", cedula)
    print("Nombre: ", nombre)
    print("Listo,",nombre," por las ",num_ham, "hamburguesas, el precio final con tarjeta es: ", total)
    print("GRACIAS POR SU COMPRA")
  else:
    print ("*****************FACTURA******************")
    print("DATOS")
    print("Cedula: ", cedula)
    print("Nombre: ", nombre)
    print("Listo, por las ",num_ham, "hamburguesas, el precio final en efectivo es: ", total)
    print("GRACIAS POR SU COMPRA")

elif tipo_ham == 3:
  a = 3.50 
  
  print("\n")
  print("Ingrese su forma de pago: ")
  print("1) Tarjeta de credito ")
  print("2) Efectivo: ")
  pago = int(input())
  
  total = a * num_ham
  
  if pago == 1:
    total = a * (num_ham) + ((a*num_ham)*5/100)
    print ("*****************FACTURA******************")
    print("DATOS")
    print("Cedula: ", cedula)
    print("Nombre: ", nombre)
    print("Listo,",nombre," por las ",num_ham, "hamburguesas, el precio final con tarjeta es: ", total)
    print("GRACIAS POR SU COMPRA")
  else:
    print ("*****************FACTURA******************")
    print("DATOS")
    print("Cedula: ", cedula)
    print("Nombre: ", nombre)
    print("Listo, por las ",num_ham, "hamburguesas, el precio final en efectivo es: ", total)
    print("GRACIAS POR SU COMPRA")
    
else:
  print("Este tipo de hamburguesa no existe")
  print("MUCHAS GRACIAS, VUELVA A INTENTARLO")