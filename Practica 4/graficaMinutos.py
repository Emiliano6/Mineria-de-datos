import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
data = pd.read_csv('P3csv´s/top_10_mensajes_por_minuto.csv')

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(data['hora_minuto'], data['cantidad_mensajes'], color='lightcoral')

# Agregar título y etiquetas
plt.title('Cantidad de mensajes por hora', fontsize=14)
plt.xlabel('Hora', fontsize=12)
plt.ylabel('Cantidad de mensajes', fontsize=12)

# Rotar las etiquetas del eje x para mejor visualización
plt.xticks(rotation=45)

# Guardar la gráfica como imagen
plt.tight_layout()
plt.savefig('grafica_cantidad_hora.png')

