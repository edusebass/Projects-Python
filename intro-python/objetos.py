class Usuario:
    nombre = "Eduardo"
    apellido = "Almachi"
usuario = Usuario()

print(usuario.nombre, usuario.apellido)  #objectos


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


usuario = Usuario('Eduardo', 'Almachi')
usuario2 = Usuario('Sebastian', 'Maisincho')

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
# esto lo utilizamos para llamar al nombre y al apellido

# METODOS

class Usuario:
    def __init__(self, nombre, apellido):
        self. nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)


usuario = Usuario('Eduardo', 'Almachi')
usuario2 = Usuario('Sebastian', 'Maisincho')

usuario.saludo()
usuario2.saludo()

# DEL ELIMINAR PROPIEDADES OBJETOS

class Usuario:
    def __init__(self, nombre, apellido):
        self. nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)


usuario = Usuario('Eduardo', 'Almachi')
usuario2 = Usuario('Sebastian', 'Maisincho')

usuario.saludo()
usuario2.saludo()


# HERENCIA
# sirve para utilizar los mismos parametros de usuario como admin
class Usuario:
    def __init__(self, nombre, apellido):
       self. nombre = nombre
       self.apellido = apellido

    def saludo(self):
       print('Hola, mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
       print('Hola, me llamo', self.nombre, 'y soy administrador de esto')

usuario = Usuario('Eduardo', 'Almachi')

usuario.saludo()
usuario.nombre = 'rita'
usuario.saludo()

admin = Admin('super', 'feliz')
admin.saludo()
admin.superSaludo()

usuario.supersaludo() 









from importlib.metadata import packages_distributions


class Animal: 
    def __init__(self, nombre, onomatopeya):      
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya )

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Soy un perro extendido')

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Soy un gato bien extendido')

class Canario(Animal):
    tipo = 'canario'

class Caballo(Animal):
    tipo = 'caballo'


perro = Perro('Rita', 'aullido')
perro.saludo()

gato = Gato('mishel','maullido')
gato.saludo()

canario = Canario('piolin', 'silbido')
canario.saludo()

caballo = Caballo('spirit', 'berrinchido')
caballo.saludo()




