import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Cargamos el CSV
df = pd.read_csv('df_whastapp_2.csv')

# 1. Longitud del mensaje
df['longitud_mensaje'] = df['mensaje'].apply(len)

# 2. Frecuencia de mensajes por autor
frecuencia_autor = df['autor'].value_counts().to_dict()
df['frecuencia_autor'] = df['autor'].map(frecuencia_autor)

# 3. Convertimos la hora a segundos desde medianoche
def hora_a_segundos(hora):
    h, m, s = map(int, hora.split(':'))
    return h * 3600 + m * 60 + s

df['hora_segundos'] = df['hora'].apply(hora_a_segundos)

# Seleccionamos las características para el modelo
X = df[['longitud_mensaje', 'frecuencia_autor', 'hora_segundos']]

# Convertimos las etiquetas (autores) a números
autores = df['autor'].unique()
label_to_number = {label: i for i, label in enumerate(autores)}
df['autor_numerico'] = df['autor'].map(label_to_number)
y = df['autor_numerico']

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalamos las características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Creamos y entrenamos el modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Hacemos predicciones
y_pred = knn.predict(X_test_scaled)

# Evaluamos el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Opcional: Mostramos las predicciones y los autores originales
predicciones = pd.DataFrame({'Predicción': y_pred, 'Autor Original': y_test.map({v: k for k, v in label_to_number.items()})})
print(predicciones.head())
