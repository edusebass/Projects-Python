
sin_iva = float(input("Ingrese el precio del proveedor: "))
print("\n")
porce = float(input("Ingrese el valor del porcentaje: "))
print("\n")
print("Que desea hacer: ")
print("1) + %")
print("2) - %")
accion = float(input())
if(accion == 1):
  costo = sin_iva + (sin_iva * (porce/100))
  print("Su costo + el ",porce,"% es: ", costo)
elif(accion == 2):
  costo = sin_iva - (sin_iva * (porce/100))
  print("Su costo - el ",porce,"% es: ", costo)
