from calendar import c
from optparse import Values
import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='eduardo',
    password='1751395623eduardo',
    database='prueba'
)

cursor = midb.cursor()

#LIST THE DATA
cursor.execute('select * from Usuario') #(select * from Usuario limit 1) ## serves for limit the result
resultado = cursor.fetchall()  #fetchall show all items
#                                 #fetchone show one items
print(resultado)


#SEE DEFINITIONS OF THE TABLE
cursor.execute('show create table Usuario')    # show the items on up


#INSERT DATA
sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
values = ('micorreo@correo.co.nz', 'nombreusuario', 45)

cursor.execute(sql, values)

midb.commit()

print(cursor.rowcount)


# #UPDATE DATA
sql = 'update Usuario set email = %s where id = %s'
values = ('micorreo@correo.com', 4)
cursor.execute(sql, values)

midb.commit()   


#ELIMINATE DATA

sql = 'delete from Usuario where id = %s'
values = (4, )

cursor.execute(sql, values)
midb.commit()



