import pandas as pd

data = pd.read_excel('data/data_preprocesing3.xlsx')
df = pd.DataFrame(data)

df['Translate'] = ''

df.to_excel('data/data_analisis.xlsx', index=False, header=True, columns=["Tweet", "Preprocesing", "Translate"])