import pandas as pd
from textblob import TextBlob
from googletrans import Translator
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="id", target="en")

data = pd.read_excel('data/data_analisis.xlsx')
df = pd.DataFrame(data)

x = 4500
# 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500
for text in range(498) : 
# for text in range(500) : 
    df['Translate'][x] = translator.translate(df['Preprocesing'][x])
    x+=1

df.to_excel('data/data_analisis.xlsx', index=False, header=True, columns=["Tweet", "Preprocesing", "Translate"])