c = open('chanchito.txt','a')    #'a' sirve para agregar otra linea

c.write('\n aqui agregaremos otra linea en el txt') #\n sirve para agregar a otra linea el texto

print(c.read())                    #c.read nos sirve para que en la terminal se pase todo el txt
#print(c.readline())                # c.read line   nos sirve para que lea una linea
#print(c.readline())

#for x in c:                     #for x in c ptra de manera de 1
    #print(x)   

c.close()                       #sirve para que ya nose habara la lectura de txt                        