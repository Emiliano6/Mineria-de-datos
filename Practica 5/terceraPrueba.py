import pandas as pd
from scipy.stats import kruskal

# Cargar el archivo CSV
file_path = 'df_whastapp_2.csv'
df = pd.read_csv(file_path)


# Convertir la columna de fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# Agregar una columna con el día de la semana (0=Lunes, 6=Domingo)
df['dia_semana'] = df['fecha'].dt.dayofweek

# Contar el número de mensajes por autor y día de la semana
mensajes_por_dia = df.groupby(['autor', 'dia_semana']).size().unstack(fill_value=0)

# Separar los grupos (mensajes enviados por los autores en diferentes días de la semana)
grupo_lunes = mensajes_por_dia[0]
grupo_martes = mensajes_por_dia[1]
grupo_miercoles = mensajes_por_dia[2]
grupo_jueves = mensajes_por_dia[3]
grupo_viernes = mensajes_por_dia[4]
grupo_sabado = mensajes_por_dia[5]
grupo_domingo = mensajes_por_dia[6]

# Realizar la prueba de Kruskal-Wallis
stat, p_value = kruskal(grupo_lunes, grupo_martes, grupo_miercoles, grupo_jueves, grupo_viernes, grupo_sabado, grupo_domingo)

# Mostrar los resultados
print(f'Estadístico de Kruskal-Wallis: {stat}')
print(f'Valor p: {p_value}')

# Interpretación de las hipótesis
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula (H0): Hay diferencias significativas entre los grupos.")
else:
    print("No se puede rechazar la hipótesis nula (H0): No hay diferencias significativas entre los grupos.")
