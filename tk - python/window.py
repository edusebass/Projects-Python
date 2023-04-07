from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Hola mundo')

def open():
    img = ImageTk.PhotoImage(Image.open('1.jpg'))
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l = Label(top,text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()


btn = Button(root, text='Click', command=open).pack() #put the botton in root

root.mainloop()