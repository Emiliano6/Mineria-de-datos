import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
data = pd.read_csv('P3csv´s/top_5_fechas_positivas.csv')

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(data['fecha'], data['cantidad_positivos'], marker='o', color='green', linestyle='-', linewidth=2)

# Agregar título y etiquetas
plt.title('Cantidad de mensajes positivos por fecha', fontsize=14)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Cantidad de mensajes positivos', fontsize=12)

# Rotar las etiquetas del eje X para mejor visualización
plt.xticks(rotation=45)

# Mostrar la gráfica
plt.tight_layout()
plt.savefig('grafica_lineas_mensajes_positivos.png')
