
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

# Calcular la longitud total de los mensajes por autor
longitud_total_por_autor = df.groupby('autor')['mensaje'].apply(lambda x: x.str.len().sum()).reset_index()
longitud_total_por_autor.columns = ['autor', 'longitud_total_mensajes']

# Definir las variables X (autor) e Y (longitud total de los mensajes)
X = np.arange(len(longitud_total_por_autor))  # Creamos un array numérico para el eje X
y = longitud_total_por_autor['longitud_total_mensajes']

# Crear y ajustar el modelo lineal
modelo = LinearRegression()
modelo.fit(X.reshape(-1, 1), y)

# Predecir
y_pred = modelo.predict(X.reshape(-1, 1))

# Calcular el R2
r2 = r2_score(y, y_pred)
print(f'R2 Score: {r2}')

# Graficar los datos y el modelo lineal
plt.figure(figsize=(12, 6))
plt.scatter(X, y, color='green', label='Datos reales')
plt.plot(X, y_pred, color='orange', linewidth=2, label='Modelo lineal')
plt.title('Autor vs Longitud Total de los Mensajes')
plt.xlabel('Autor')
plt.ylabel('Longitud Total de los Mensajes')
plt.xticks(X, longitud_total_por_autor['autor'], rotation=45)  # Mostrar los nombres de los autores en el eje X
plt.legend()

# Guardar la imagen
plt.savefig('regresion_autor_longitud_total.png')

# Mostrar el gráfico
plt.show()
