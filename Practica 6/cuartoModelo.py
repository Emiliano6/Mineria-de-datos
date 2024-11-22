
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
# Convertir la columna de fecha a día de la semana (0 = Lunes, 6 = Domingo)
df['fecha'] = pd.to_datetime(df['fecha'])
df['dia_semana'] = df['fecha'].dt.dayofweek

# Agrupar por día de la semana para contar la cantidad de mensajes enviados
mensajes_por_dia = df.groupby('dia_semana')['mensaje'].count().reset_index()
mensajes_por_dia.columns = ['dia_semana', 'cantidad_mensajes']

# Definir las variables X (día de la semana) e Y (cantidad de mensajes)
X = mensajes_por_dia[['dia_semana']]
y = mensajes_por_dia['cantidad_mensajes']

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
plt.title('Día de la Semana vs Cantidad de Mensajes')
plt.xlabel('Día de la Semana (0=Lunes, 6=Domingo)')
plt.ylabel('Cantidad de Mensajes')
plt.legend()

# Guardar la imagen
plt.savefig('regresion_dia_semana_cantidad_mensajes.png')

# Mostrar el gráfico
plt.show()
