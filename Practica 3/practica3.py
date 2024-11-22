import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv(r'C:\Users\emili\OneDrive\Documentos\Mineria-de-datos\df_whastapp_2.csv', encoding='utf-8')

# Limpiar la columna 'autor' (eliminar espacios al principio y final, y convertir a minúsculas)
df['autor'] = df['autor'].str.strip().str.lower()

# Agrupar por autor y contar los mensajes
df_autor_stats = df.groupby("autor").agg({
    'mensaje': ['count'],  # Contar cuántos mensajes ha enviado cada autor
}).reset_index()

# Renombrar las columnas para mayor claridad
df_autor_stats.columns = ['autor', 'total_mensajes']

# Guardar los resultados en un nuevo archivo CSV
df_autor_stats.to_csv("MensajesPorAutor.csv", index=False)

df['datetime'] = pd.to_datetime(df['fecha'] + ' ' + df['hora'], dayfirst=True)

# Extraer la hora y los minutos de la columna 'datetime'
df['hora_extraida'] = df['datetime'].dt.hour
df['minuto_extraido'] = df['datetime'].dt.minute

# Contar cuántos mensajes se enviaron en cada minuto de cada hora
mensajes_por_minuto = df.groupby(['hora_extraida', 'minuto_extraido']).size().reset_index(name='cantidad_mensajes')

# Crear una nueva columna combinando la hora y el minuto
mensajes_por_minuto['hora_minuto'] = mensajes_por_minuto['hora_extraida'].astype(str) + ':' + mensajes_por_minuto['minuto_extraido'].astype(str).str.zfill(2)

# Ordenar los resultados por la cantidad de mensajes y seleccionar el top 10
top_10_mensajes = mensajes_por_minuto.sort_values(by='cantidad_mensajes', ascending=False).head(10)

# Eliminar las columnas 'hora_extraida' y 'minuto_extraido'
top_10_mensajes = top_10_mensajes.drop(columns=['hora_extraida', 'minuto_extraido'])

# Guardar el top 10 en un CSV
top_10_mensajes.to_csv('top_10_mensajes_por_minuto.csv', index=False)


df['datetime'] = pd.to_datetime(df['fecha'] + ' ' + df['hora'], dayfirst=True)

# Extraer solo la fecha (día, mes, año)
df['fecha_extraida'] = df['datetime'].dt.strftime('%d/%m/%Y')

# Contar cuántos mensajes se enviaron en cada día
mensajes_por_dia = df.groupby('fecha_extraida').size().reset_index(name='cantidad_mensajes')

# Ordenar los resultados por la cantidad de mensajes y seleccionar el top 10
top_10_dias = mensajes_por_dia.sort_values(by='cantidad_mensajes', ascending=False).head(10)

# Guardar el top 10 en un CSV
top_10_dias.to_csv('top_10_dias_con_mas_mensajes.csv', index=False)

# Calcular la longitud de cada mensaje
df['longitud_mensaje'] = df['mensaje'].apply(len)

# Agrupar por autor y calcular la longitud promedio de los mensajes
longitud_promedio_usuario = df.groupby('autor')['longitud_mensaje'].mean().reset_index()

# Guardar el resultado en un CSV
longitud_promedio_usuario.to_csv('longitud_promedio_mensajes_por_usuario.csv', index=False)