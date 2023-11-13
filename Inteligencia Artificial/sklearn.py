import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#leer archivos
datos = pd.read_csv("Salary_Data1.csv")
#muestra las 5 primeras filas
datos.head()
#caracteristicas basicas estadisticas
datos.describe()

#separar datos de entrada X son caracteristicas y Y son etiquetas
x = datos[['YearsExperience']]
y = datos[['Salary']]

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

