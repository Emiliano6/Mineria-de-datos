import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Inicializar VADER
sia = SentimentIntensityAnalyzer()

# Cargar el CSV
ruta_csv = 'df_whastapp_2.csv'
df = pd.read_csv(ruta_csv)

# Asegurarse de que la columna 'fecha' esté en formato de fecha
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

# Función para analizar el sentimiento con VADER
def analizar_sentimiento_vader(mensaje):
    sentiment_score = sia.polarity_scores(mensaje)
    if sentiment_score['compound'] > 0:
        return 'positivo'
    elif sentiment_score['compound'] < 0:
        return 'negativo'
    else:
        return 'neutral'

# Aplicar la función de análisis de sentimiento a la columna 'mensaje'
df['sentimiento'] = df['mensaje'].apply(analizar_sentimiento_vader)

# Agrupar por autor y sentimiento, contar los mensajes y total
resumen_sentimientos_autor = df.groupby(['autor', 'sentimiento']).size().unstack(fill_value=0).reset_index()

# Agregar la columna con el total de mensajes enviados por autor
resumen_sentimientos_autor['total_mensajes'] = resumen_sentimientos_autor[['positivo', 'negativo', 'neutral']].sum(axis=1)

# Guardar el resumen por autor en un CSV
resumen_sentimientos_autor.to_csv('resumen_mensajes_por_autor.csv', index=False)

# Filtrar mensajes negativos
mensajes_negativos = df[df['sentimiento'] == 'negativo']

# Agrupar los mensajes negativos por fecha y contar
conteo_negativos = mensajes_negativos.groupby('fecha').size().reset_index(name='cantidad_negativos')

# Obtener el top 5 de fechas con más mensajes negativos
top_5_negativos = conteo_negativos.sort_values(by='cantidad_negativos', ascending=False).head(5)

# Guardar el top 5 en un CSV
top_5_negativos.to_csv('top_5_fechas_negativas.csv', index=False)

# Filtrar mensajes positivos
mensajes_positivos = df[df['sentimiento'] == 'positivo']

# Agrupar los mensajes positivos por fecha y contar
conteo_positivos = mensajes_positivos.groupby('fecha').size().reset_index(name='cantidad_positivos')

# Obtener el top 5 de fechas con más mensajes positivos
top_5_positivos = conteo_positivos.sort_values(by='cantidad_positivos', ascending=False).head(5)

# Guardar el top 5 en un CSV
top_5_positivos.to_csv('top_5_fechas_positivas.csv', index=False)
