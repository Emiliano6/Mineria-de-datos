import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Cargar el archivo CSV (ajustar la ruta si es necesario)
df = pd.read_csv('df_whastapp_2.csv')

df['longitud_mensaje'] = df['mensaje'].apply(len)

# Escalamos los datos para que estén en la misma escala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['longitud_mensaje']])  # Usamos longitud de mensaje como ejemplo

# Aplicamos K-Means con el número de clusters que creas conveniente (en este caso 6)
kmeans = KMeans(n_clusters=6, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualización de los clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x=range(len(df)), y='longitud_mensaje', hue='cluster', palette='Set1')
plt.title('Clustering de Mensajes usando K-Means')
plt.xlabel('Índice de Mensaje')
plt.ylabel('Longitud del Mensaje')

# Guardar la imagen
plt.savefig('clusters_mensajes.png')

# Mostrar algunas filas del dataframe con los clusters asignados
print(df[['autor', 'mensaje', 'longitud_mensaje', 'cluster']].head(10))
