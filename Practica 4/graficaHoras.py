import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
data = pd.read_csv('P3csv´s/longitud_promedio_mensajes_por_usuario.csv')

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(data['autor'], data['longitud_mensaje'], color='skyblue')

# Agregar título y etiquetas
plt.title('Longitud de los mensajes por autor', fontsize=14)
plt.xlabel('Autor', fontsize=12)
plt.ylabel('Longitud del mensaje', fontsize=12)

# Rotar las etiquetas del eje x para mejor visualización
plt.xticks(rotation=45)

# Guardar la gráfica como imagen
plt.tight_layout()
plt.savefig('grafica_longitud_mensajes.png')
