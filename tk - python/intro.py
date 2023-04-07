from cProfile import label
from tkinter import *


root =Tk() #!
root.title('Hola mundo') #title interfaz
root.geometry('500x500') #dimensions



#label = Label(root, text='Holamundo! mi primera etiqueta')
#label.pack()

l1 = Label(root, text='Hola mundo! primera etiqueta')
l2 = Label(root, text='Chao mundo! segunda etiqueta')

l1.grid(row=0, column=0)
l2.grid(row=1, column=1)

root.mainloop() #!