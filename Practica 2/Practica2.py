import pandas as pd

# Cargar el CSV
ruta_csv = 'df_whastapp.csv'
df = pd.read_csv(ruta_csv)

# Convertir las columnas 'fecha' y 'hora' a un solo campo de tipo datetime
df['datetime'] = pd.to_datetime(df['fecha'] + ' ' + df['hora'], dayfirst=True)

# Ordenar el dataframe por la nueva columna 'datetime'
df_sorted = df.sort_values(by='datetime')

# Guardar el archivo CSV ordenado
df_sorted.to_csv('df_whastapp_2.csv', index=False)

print("Archivo ordenado correctamente.")
