from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Hola mundo')

tree = ttk.Treeview(root)
tree['columns'] =('Nombre', 'Telefono', 'Empresa')

tree.column('#0')
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('#0', text='id')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=0)

tree.insert('', END, 'lala', values=('Uno', 'Dos', 'Tres'), text='Chanchito feliz')
tree.insert('', END, 'lele', values=('1', '2', '3'), text='Eduardo Happy')
root.mainloop()