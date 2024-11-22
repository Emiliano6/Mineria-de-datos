import matplotlib.pyplot as plt
import pandas as pd

# Cargar el CSV recién generado
df_mensajes_por_mes = pd.read_csv('P3csv´s/mensajes_por_mes.csv')

# Convertir la columna year_month a un formato de fecha para ordenar bien en el gráfico
df_mensajes_por_mes['year_month'] = pd.to_datetime(df_mensajes_por_mes['year_month'].astype(str))

# Crear gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(df_mensajes_por_mes['year_month'].dt.strftime('%Y-%m'), df_mensajes_por_mes['cantidad_mensajes'], color='skyblue')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Mensajes')
plt.title('Cantidad de Mensajes por Mes (Jul 2023 - Nov 2024)')
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar la gráfica como imagen
plt.savefig('mensajes_por_mes.png')

# Mostrar la gráfica
plt.show()