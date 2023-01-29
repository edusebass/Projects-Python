import os
from os import system
# print("------------------LOGIN - AMAZON-------------------------")
# email = str(input("Ingrese tu email: "))
# password = input("Ingrese su contraseña: ")
# while password != "Secret*" or email != "tosh@gmail.com":
#   print("----------ERROR CREDENCIALES INCORRECTAS")
#   print("Ingresa nuevamente las credenciales")
#   email = str(input("Ingrese tu email: "))
#   password = input("Ingrese su contraseña: ")
# system("clear")

contproductos = 0
sumnumproductos = 0
sumaproductos = 0
sumaproductosdesc = 0
productoscondesc = 0
productossindesc = 0

print("----------------BIENVENIDO A AMAZON-------------------------")
opcion = int(input("Menu de opciones \n1.-Ingresar productos al carrito de Amazon \n2.-Facturar \n3.-Salir \nIngrese opcion: "))
system("clear")
while opcion != 3:
  if opcion == 1:
    numproductos = int(input("Ingrese el numero de productos a registrar: "))
    while sumnumproductos < numproductos:
      tienedescuento = str(input(f"El producto {sumnumproductos + 1} tiene cupon de descuentos?: \nsi o no?: "))
      if tienedescuento == "si":
        cupondescuento = str(input("Ingrese el codigo el producto: "))
        while cupondescuento != "enero":
          cupondescuento = str(input("Ingrese el cupon correcto: "))
        precioproducto = float(input("Ingrese el precio del producto: "))
        preciocondesc = precioproducto * 0.50
        sumaproductosdesc += preciocondesc
        productoscondesc += 1                       
      else:
        precioproducto = float(input("Ingrese el precio del producto: "))                    
        sumaproductos += precioproducto
        productossindesc += 1
      sumnumproductos +=1 #esto es para el while
    contproductos += sumnumproductos
    system("clear")

  if opcion == 2:
    print("\n-----------FACTURA ELECTRONICA--------")
    print("La factura sera enviada a su correo electronico")
    if productoscondesc > 0:
      print("----------------Descuento----------")
      print("\t*Detalle del cupon de descuento")
      print("\t*Nombre del cupon de descuento es enero")
      print(f"\t*El numero de productos con descuento es: {productoscondesc}")
      print(f"\t*El precio final de la compra es: {sumaproductosdesc + sumaproductos}")
    else:
      print(f"\t*El numero de productos son: {contproductos}")
      print(f"\t*El precio final de la compra es: {sumaproductos} ")
  opcion = int(input("\n----------------BIENVENIDO A AMAZON-------------------------\nMenu de opciones \n1.-Ingresar productos al carritode Amazon \n2.-Facturar \n3.-Salir \nIngrese opcion: "))
system("clear") 
print("GRACIAS POR SU COMPRA, HASTA LUEGO")