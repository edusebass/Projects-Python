from tkinter import *

root = Tk()
root.title('Hola mundo')


l = Label(root, text='Hola mundo')
def click():                            #funtion of string later clicking
    l.pack()

btn = Button(root, text="Clickeame", command=click, fg="red", bg='blue') #button configuration
btn.pack()


root.mainloop()