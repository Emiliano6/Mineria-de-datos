import pandas as pd
from scipy.stats import kruskal

# Cargar el archivo CSV
file_path = 'df_whastapp_2.csv'
df = pd.read_csv(file_path)

# Contar el número de mensajes por cada autor
mensajes_por_autor = df['autor'].value_counts().reset_index()
mensajes_por_autor.columns = ['autor', 'total_mensajes']

# Dividir a los autores en cuartiles según el número de mensajes
mensajes_por_autor['cuartil'] = pd.qcut(mensajes_por_autor['total_mensajes'], 4, labels=["Q1", "Q2", "Q3", "Q4"])

# Separar los grupos según los cuartiles
grupo_Q1 = mensajes_por_autor[mensajes_por_autor['cuartil'] == "Q1"]['total_mensajes']
grupo_Q2 = mensajes_por_autor[mensajes_por_autor['cuartil'] == "Q2"]['total_mensajes']
grupo_Q3 = mensajes_por_autor[mensajes_por_autor['cuartil'] == "Q3"]['total_mensajes']
grupo_Q4 = mensajes_por_autor[mensajes_por_autor['cuartil'] == "Q4"]['total_mensajes']

# Realizar la prueba de Kruskal-Wallis
stat, p_value = kruskal(grupo_Q1, grupo_Q2, grupo_Q3, grupo_Q4)

# Mostrar el resultado
print(f'Estadístico de Kruskal-Wallis: {stat}')
print(f'Valor p: {p_value}')

# Interpretación de las hipótesis
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula (H0): Hay diferencias significativas entre los grupos.")
else:
    print("No se puede rechazar la hipótesis nula (H0): No hay diferencias significativas entre los grupos.")



