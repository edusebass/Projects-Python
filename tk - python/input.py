from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry("500x500")

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresar texto:")

def click():
    texto = e.get()
    # l = Label(root, text=texto)  
    # l.pack()
    # e.delete(0, END) #?delete the text of input

    # texto = e.get()
    # l = Label(root, text=texto) #?acumulate the text 
    # l.pack()

    # texto = e.get()
    # # l.configure(text=texto) #? change de text

btn = Button(root, text='click',command=click)
btn.pack()


l = Label(root, text='Texto de la etiqueta') #put text of etiquet
l.pack()

root.mainloop()