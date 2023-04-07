from tkinter import *

root = Tk()
root.title('HOLA MUNDO: OPTION MENU')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'Eduardo Almachi',
    'Eduardo Sebastian',
    'Eduardo Maisincho'
]

value = StringVar()
value.set(lista[1])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
