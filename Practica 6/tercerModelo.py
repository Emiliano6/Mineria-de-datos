
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

# Convertir la columna 'hora' a valores numéricos (de 0 a 23)
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S').dt.hour

# Agrupar por hora para obtener la cantidad de mensajes enviados en cada hora
mensajes_por_hora = df.groupby('hora')['mensaje'].count().reset_index()
mensajes_por_hora.columns = ['hora', 'cantidad_mensajes']

# Definir X (hora) e Y (cantidad de mensajes) para el modelo lineal
X = mensajes_por_hora[['hora']]
y = mensajes_por_hora['cantidad_mensajes']

# Crear y ajustar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir
y_pred = modelo.predict(X)

# Calcular el R2
r2 = r2_score(y, y_pred)
print(f'R2 Score: {r2}')

# Graficar los datos y el modelo lineal
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='green', label='Datos reales')
plt.plot(X, y_pred, color='orange', linewidth=2, label='Modelo lineal')
plt.title('Hora del Día vs Cantidad de Mensajes')
plt.xlabel('Hora del Día')
plt.ylabel('Cantidad de Mensajes')
plt.legend()

# Guardar la imagen
plt.savefig('regresion_hora_cantidad_mensajes.png')


