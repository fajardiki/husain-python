import pandas as pd
import numpy as np
from ast import literal_eval

# PERSIAPAN DATA
data = pd.read_excel('data/data_preprocesing2.xlsx')
# data = pd.read_excel('data/data_preprocesing2.xlsx', usecols=["Tweet", "Stemmer"])
df = pd.DataFrame(data)
df['Stemmer'] = df['Stemmer'].apply(literal_eval)

# MENGEMBALIKAN DATA HASIL TOKENIZING DAN REMOVAL STOPWORD
def fit_stopword(text) :
    text = np.array(text)
    text = ' '.join(text)
    return text
df['Preprocesing'] = df['Stemmer'].apply(lambda x: fit_stopword(x))

# df.drop_duplicates().reset_index(drop=True)
df.to_excel('data/data_preprocesing3.xlsx', index=False, header=True)
# print(df.dropna())