from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')

def click():
               #showwarning
            #    showinfo
            # showerror
    messagebox.askquestion('Popup', 'Hola mundo')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()