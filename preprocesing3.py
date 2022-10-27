import numpy as np
import pandas as pd

from ast import literal_eval

data = pd.read_excel('data/data_preprocesing2.xlsx')
df = pd.DataFrame(data)

df['Stemmer'] = df['Stemmer'].apply(literal_eval)

# MENGEMBALIKAN DATA HASIL TOKENIZING DAN REMOVAL STOPWORD
def fit_stopword(text) :
    text = np.array(text)
    text = ' '.join(text)
    return text
df['Preprocesing'] = df['Stemmer'].apply(lambda x: fit_stopword(x))

df.to_excel('data/data_preprocesing3.xlsx', columns=['Tweet', 'Stemmer', 'Preprocesing'], header=True, index=False)