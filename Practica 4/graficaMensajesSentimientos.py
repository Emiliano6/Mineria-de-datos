import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
data = pd.read_csv('P3csv´s/resumen_mensajes_por_autor.csv')

# Crear la gráfica apilada
plt.figure(figsize=(10, 6))
plt.bar(data['autor'], data['negativo'], label='Negativo', color='red')
plt.bar(data['autor'], data['neutral'], bottom=data['negativo'], label='Neutral', color='gray')
plt.bar(data['autor'], data['positivo'], bottom=data['negativo'] + data['neutral'], label='Positivo', color='green')

# Agregar título y etiquetas
plt.title('Distribución de mensajes por sentimiento y autor', fontsize=14)
plt.xlabel('Autor', fontsize=12)
plt.ylabel('Cantidad de mensajes', fontsize=12)

# Agregar leyenda
plt.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.savefig('grafica_apilada_sentimientos.png')

