import pandas as pd
from scipy.stats import kruskal

# Cargar el archivo CSV con la longitud promedio de mensajes
file_path = 'P3csv´s/longitud_promedio_mensajes_por_usuario.csv'
df = pd.read_csv(file_path)

# Dividir los autores en cuartiles según la longitud promedio de sus mensajes
df['cuartil'] = pd.qcut(df['longitud_mensaje'], 4, labels=["Q1", "Q2", "Q3", "Q4"])

# Separar los grupos según los cuartiles
grupo_Q1 = df[df['cuartil'] == "Q1"]['longitud_mensaje']
grupo_Q2 = df[df['cuartil'] == "Q2"]['longitud_mensaje']
grupo_Q3 = df[df['cuartil'] == "Q3"]['longitud_mensaje']
grupo_Q4 = df[df['cuartil'] == "Q4"]['longitud_mensaje']

# Realizar la prueba de Kruskal-Wallis
stat, p_value = kruskal(grupo_Q1, grupo_Q2, grupo_Q3, grupo_Q4)

# Mostrar los resultados
print(f'Estadístico de Kruskal-Wallis: {stat}')
print(f'Valor p: {p_value}')

# Interpretación de las hipótesis
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula (H0): Hay diferencias significativas entre los grupos.")
else:
    print("No se puede rechazar la hipótesis nula (H0): No hay diferencias significativas entre los grupos.")
