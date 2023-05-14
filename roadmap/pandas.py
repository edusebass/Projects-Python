import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Laura'],
    'Edad': [25, 30, 18, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Filtrar por edad
mayores_edad = df[df['Edad'] >= 18]
print(mayores_edad)

# Calcular estadísticas
promedio_edad = df['Edad'].mean()
print("Promedio de edad:", promedio_edad)

# Guardar el DataFrame en un archivo CSV
df.to_csv('datos.csv', index=False)