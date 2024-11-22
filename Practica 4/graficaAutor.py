import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
data = pd.read_csv('P3csv´s/MensajesPorAutor.csv')

# Crear el gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(data['total_mensajes'], labels=data['autor'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

# Agregar título
plt.title('Proporción de mensajes por autor', fontsize=14)

# Mostrar la gráfica
plt.tight_layout()
plt.savefig('grafica_pastel_mensajes.png')

