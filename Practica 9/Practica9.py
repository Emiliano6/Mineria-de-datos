import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import numbers

# Función para obtener las x numéricas, transformando la fecha en valores numéricos
def transform_variable(df: pd.DataFrame, x:str) -> pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        # Convertimos la fecha a formato numérico en segundos desde la época (1970-01-01)
        return pd.to_datetime(df[x]).astype(np.int64) / 10**9  # Convertimos la fecha a formato numérico

# Función para hacer la predicción usando regresión lineal
def linear_reg(df: pd.DataFrame, x:str, y: str) -> dict:  # Cambié Dict a dict
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
    print(model.summary())
    coef = model.params
    m = coef[1]  # Pendiente
    b = coef[0]  # Intercepto
    r2 = model.rsquared  # R2
    r2_adj = model.rsquared_adj  # R2 ajustado
    return {'m': m, 'b': b, 'r2': r2, 'r2_adj': r2_adj}

# Función para graficar la regresión lineal y las predicciones
def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, filename: str):
    fixed_x = transform_variable(df, x)
    plt.figure(figsize=(10, 6))
    plt.scatter(fixed_x, df[y], color='blue', label='Datos Reales')
    plt.plot(fixed_x, m * fixed_x + b, color='green', label='Regresión Lineal')
    plt.title('Predicción de Mensajes a lo largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Mensajes')
    plt.legend()
    plt.savefig(filename)  # Guardar la imagen en un archivo
    plt.close()  # Cerrar la figura para evitar mostrarla en pantalla

# Cargar el archivo CSV df_whatsapp_2.csv
df = pd.read_csv('df_whastapp_2.csv')

# Limpiar los datos
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')  # Asegúrate de que la columna 'fecha' esté en formato datetime
df_grouped = df.groupby('fecha').size().reset_index(name='num_mensajes')  # Agrupar por fecha y contar los mensajes

# Realizar la regresión para predecir el número de mensajes a lo largo del tiempo
lin = linear_reg(df_grouped, "fecha", "num_mensajes")

# Guardar la regresión en un archivo de imagen
plt_lr(df_grouped, "fecha", "num_mensajes", lin['m'], lin['b'], 'prediccion_mensajes.png')

# Predicciones para fechas futuras (por ejemplo, los próximos 5 días)
# Crear un rango de fechas futuras para hacer las predicciones
last_date = df_grouped['fecha'].max()
future_dates = pd.date_range(last_date, periods=6, freq='D')  # Predicción para los próximos 5 días

# Convertir las fechas futuras en valores numéricos para la predicción
future_dates_numeric = (future_dates.astype(np.int64) / 10**9)

# Realizar la predicción usando el modelo entrenado
predictions = lin['m'] * future_dates_numeric + lin['b']

# Mostrar las predicciones
pred_df = pd.DataFrame({
    'Fecha': future_dates,
    'Predicción de Mensajes': predictions
})

print("Predicciones para los próximos días:")
print(pred_df)
