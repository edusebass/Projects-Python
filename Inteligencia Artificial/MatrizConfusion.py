import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

#leer archivos
datos = pd.read_csv("diabetes_prediction_dataset.csv")
#muestra las 5 primeras filas
datos.head()
#caracteristicas basicas estadisticas
datos.describe()

#separar datos de entrada X son caracteristicas y Y son etiquetas
x = datos.iloc[:, :-1] #todas las columnas menos la ultima
y = datos.iloc[:, -1] # ultima columna

#dividir los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=25)

#crear modelo con arbol de decision
modelo = DecisionTreeClassifier()

#entrenar modelo con arbol de decision
modelo.fit(x_train, y_train)

#probar el modelo con los datos de prueba
y_obt = modelo.predict(x_test)

#Evaluar el modelo con las metricas, r2= coeficiente de determinacion
exactitud = accuracy_score(y_test, y_obt)
print("La exactitud es: ", exactitud)

Matriz_confusion = confusion_matrix(y_test, y_obt)

#crear mapa de calor de la matriz de confusion
sns.heatmap(Matriz_confusion, fmt="d", cmap="viridis", annot=True)
plt.show()
#realizar una nueva prediccion
diabetes = modelo.predict([[1, 40, 1, 1, 1,30, 6.6, 150]])
print("1: Tiene diabetes y 0: no tiene diabetes: ", diabetes)

#ESTO NO IRIA EN UNA MATRIZ DE CONFUSION
# #imprimir los coeficientes de regresion
# print("El coeficiente B1 es: ", modelo.coef_)
# print("La intercepcion es: ", modelo.intercept_)

# #crear una grafica de dispersion
# plt.scatter(x['pH'], y)
# plt.title("Regresion Lineal")
# plt.xlabel("ph")
# plt.ylabel("Calidad")
# plt.show()

# #grafica de los valores obtenidos y los valores reales
# #Crear una lista desde 1 hasta la longitud de ytest
# lista = [i for i in range(1, len(y_test)+ 1,1)]
# plt.plot(lista, y_test, color="r")
# plt.plot(lista, y_obt)
# plt.show()
