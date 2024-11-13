import pandas as pd
from tabulate import tabulate

df = pd.read_csv('C:/Users/emili/OneDrive/Documentos/Mineria-de-datos/df_whastapp.csv')
print(tabulate(df, headers='keys', tablefmt='pretty'))
