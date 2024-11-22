import pandas as pd

# Cargar tu archivo CSV que contiene los mensajes
ruta_csv = 'df_whastapp_2.csv'
df = pd.read_csv(ruta_csv)

# Convertir la columna de fecha en formato de fecha de pandas (si no lo está ya)
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# Crear una nueva columna que contenga solo el año y mes
df['year_month'] = df['fecha'].dt.to_period('M')

# Agrupar por año y mes y contar la cantidad de mensajes por mes
mensajes_por_mes = df.groupby('year_month').size().reset_index(name='cantidad_mensajes')

# Guardar en un nuevo CSV
mensajes_por_mes.to_csv('mensajes_por_mes.csv', index=False)
