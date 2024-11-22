import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np

# Cargar el archivo CSV df_whastapp_2
file_path = 'df_whastapp_2.csv'
df = pd.read_csv(file_path)

# Convertir la columna 'hora' a un valor numérico de horas (de 0 a 23) para usarla como variable independiente
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S').dt.hour

# Calcular la longitud de los mensajes (como una posible variable dependiente)
df['longitud_mensaje'] = df['mensaje'].str.len()

# Seleccionamos las variables para el modelo lineal: X (hora) y Y (longitud del mensaje)
X = df[['hora']]
y = df['longitud_mensaje']

# Dividir los datos en conjunto de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir sobre los datos de prueba
y_pred = modelo.predict(X_test)

# Calcular el R2 del modelo
r2 = r2_score(y_test, y_pred)
print(f'R2 Score: {r2}')

# Graficar los puntos de datos y la línea de regresión
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Modelo lineal')
plt.title('Regresión Lineal: Hora del Día vs Longitud del Mensaje')
plt.xlabel('Hora del Día')
plt.ylabel('Longitud del Mensaje')
plt.legend()

# Guardar la imagen
plt.savefig('regresion_lineal_hora_longitud_mensaje.png')


# Crear un gráfico de dispersión para visualizar la correlación
plt.figure(figsize=(10, 6))
plt.scatter(df['hora'], df['longitud_mensaje'], color='green', alpha=0.5)
plt.title('Gráfico de dispersión: Hora del Día vs Longitud del Mensaje')
plt.xlabel('Hora del Día')
plt.ylabel('Longitud del Mensaje')

# Guardar la imagen
plt.savefig('dispersion_hora_longitud_mensaje.png')


