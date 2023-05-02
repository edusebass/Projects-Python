import turtle

def arbol_pitagoras(longitud, nivel):
    if nivel == 0:
        return
    turtle.forward(longitud)
    turtle.left(45)
    arbol_pitagoras(longitud * 0.6, nivel - 1)
    turtle.right(90)
    arbol_pitagoras(longitud * 0.6, nivel - 1)
    turtle.left(45)
    turtle.backward(longitud)

turtle.speed('fastest')
turtle.left(90)
arbol_pitagoras(100, 8)