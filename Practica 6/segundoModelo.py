import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np

file_path = 'df_whastapp_2.csv'
df = pd.read_csv(file_path)


# Cargar el archivo CSV
df = pd.read_csv(file_path)

# Agrupar por autor para obtener la cantidad de mensajes y la longitud promedio de los mensajes por autor
mensajes_por_autor = df.groupby('autor')['mensaje'].count().reset_index()
mensajes_por_autor.columns = ['autor', 'cantidad_mensajes']

longitud_promedio_por_autor = df.groupby('autor')['mensaje'].apply(lambda x: x.str.len().mean()).reset_index()
longitud_promedio_por_autor.columns = ['autor', 'longitud_promedio_mensaje']

# Unir ambos DataFrames por el autor
df_autores = pd.merge(mensajes_por_autor, longitud_promedio_por_autor, on='autor')

# Definir las variables X e Y para el modelo
X = df_autores[['cantidad_mensajes']]
y = df_autores['longitud_promedio_mensaje']

# Crear y ajustar el modelo lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir
y_pred = modelo.predict(X)

# Calcular el R2
r2 = r2_score(y, y_pred)
print(f'R2 Score: {r2}')

# Graficar los datos y el modelo lineal
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', linewidth=2, label='Modelo lineal')
plt.title('Cantidad de Mensajes vs Longitud Promedio de Mensajes')
plt.xlabel('Cantidad de Mensajes')
plt.ylabel('Longitud Promedio del Mensaje')
plt.legend()

# Guardar la imagen
plt.savefig('regresion_cantidad_longitud_mensaje.png')
