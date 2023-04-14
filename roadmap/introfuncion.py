'''INTRODUCCION FUNCIONES'''

import os
# DECLARA TUS VARIABLES 👻
nombreUsuario = "BYRON"
# SOLICITA DATOS AL USUARIO 🤠
print("Cargando datos...")
print("Hola,",nombreUsuario)
print("Seleccione un día para la actividad planificada")
print("1) Lunes 2) Martes 3) Miércoles 4) Jueves 5) Viernes")
numeroActividad=int(input("Ingrese el día: "))

#REALIZA EL PROCEDIMIENTO 🔎
# IMPRIME LOS RESULTADOS 💡
def actividadSiri(numeroActividad):
    if numeroActividad == 1:
        return print("Genial ", nombreUsuario,"tu debes hacer ejercicios")
    elif numeroActividad == 2:
        return print("Genial ", nombreUsuario,"tu debes hacer las compras")
    elif numeroActividad == 3:
        return print("Genial ", nombreUsuario,"tu debes ver películas")
    elif numeroActividad == 4:
        return print("Genial ", nombreUsuario,"tu debes hacer deberes")
    elif numeroActividad == 5:
        return print("Genial ", nombreUsuario,"tu debes jugar fútbol")
    else:
        return print("Hey",nombreUsuario,"no existe actividad para el número ingresado")

actividadSiri(numeroActividad)
# GENIAL ERES UN EXCELENTE PROGRAMADOR(A)⭐


