from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

# imagen = Image.open('gato.jpg')   open the navigator from system
# imagen.show()

img = ImageTk.PhotoImage(Image.open('gato.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()


