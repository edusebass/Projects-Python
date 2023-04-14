'''
Un contador 
  Es una variable que se utiliza para contar algo. 
  Normalmente usamos un contador dentro de un ciclo y cambiamos su valor sumándole o
  restándole una constante, es decir, siempre se le suma o resta la misma cantidad. 

  * El caso más utilizado es incrementar la variable en uno.


  Un ejemplo 
  Al visitar el departamento de servicio al cliente en una empresa, los clientes deben tomar 
  un ticket para obtener un turno. 
  
  Por otra parte, existe un letrero electrónico que indica el número del cliente que se está atendiendo, cuando 
  éste número cambia incrementándose en 1 para anunciar el siguiente turno a ser atendido.


  Con el ejemplo, se observan  ciertas características de contadores:

  *--> Siempre tienen un valor inicial
  *--> Su valor nuevo es el resultado del valor anterior más una constante.
  
  Al inicio del día, el contador debe ser inicializado, de preferencia con 0, cuando un puesto de atención 
  está listo para atención, el contador se incrementa en uno, suena una alerta, y se procede a atender al primer turno.

'''

contador = 10
contador = contador - 1
print("El turno para la atención es: ",contador)



'''
  Un contador decreciente 
  Se encuentra en un cronometro, por ejemplo del microondas, en el que el valor inicial son los 
  segundos que permanecerá encendido. 
  El contador de tiempo disminuye en uno cada segundo y al llegar a 0 se apaga el microondas.
'''

contadorMicro = 10
contadorMicro = contadorMicro - 1
if contadorMicro == 0:
  print("La comida esta lista para servir y disfrutrar ")
else:
  print(contadorMicro)



monedas = 300
vidas = 3

if monedas>=100:
  vidas += 1
  print("El número de vidas del jugador es: ",vidas)


'''
  Finalmente:
    Un contador es una variable cuyo valor se incrementa o decrementa en una cantidad 
    constante cada vez que se produce un determinado suceso o acción.
'''