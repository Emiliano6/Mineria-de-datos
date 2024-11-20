import pandas as pd

# Leer el archivo CSV asegurando la correcta codificación para acentos y 'Ñ'
df = pd.read_csv(r'C:\Users\emili\OneDrive\Documentos\Mineria-de-datos\df_whastapp.csv', encoding='utf-8')

# Separar por columnas (suponiendo que el archivo ya esté organizado de forma limpia)
df.columns = ['fecha', 'hora', 'autor', 'mensaje']

# Mostrar las primeras filas para verificar
print(df.head())
