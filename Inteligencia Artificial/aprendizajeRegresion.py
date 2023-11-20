import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#leer archivos
datos = pd.read_excel("WSHouse.xlsx")
#muestra las 5 primeras filas
datos.head()
#caracteristicas basicas estadisticas
datos.describe()

#separar datos de entrada X son caracteristicas y Y son etiquetas
x = datos[['Tamanio']]
y = datos[['Precio_venta']]

#dividir los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=25)

#crear modelo
modelo = LinearRegression()

#entrenar modelo
modelo.fit(x_train, y_train)

#probar el modelo con los datos de prueba
y_obt = modelo.predict(x_test)

#Evaluar el modelo con las metricas
error = mean_squared_error(y_test, y_obt)
print("El error es: ", error)

r2 = r2_score(y_test, y_obt)
print("El coeficiente de determinacion es: ", r2)

#realizar una nueva prediccion
salario = modelo.predict([[2]])
print("EL salario es: ", salario)

#imprimir los coeficientes de regresion
print("El coeficiente B1 es: ", modelo.coef_)
print("La intercepcion es: ", modelo.intercept_)

#crear una grafica de dispersion
plt.scatter(x['Tamanio'], y)
plt.title("Regresion Lineal")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.show()

#grafica de los valores obtenidos y los valores reales
#Crear una lista desde 1 hasta la longitud de ytest
lista = [i for i in range(1, len(y_test)+ 1,1)]
plt.plot(lista, y_test, color="r")
plt.plot(lista, y_obt)
plt.show()
