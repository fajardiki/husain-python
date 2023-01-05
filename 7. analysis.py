import pandas as pd
from textblob import TextBlob
from googletrans import Translator
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="id", target="en")

data = pd.read_excel('data/data_analisis.xlsx')
df = pd.DataFrame(data)

df.to_excel('data/data_analisis2.xlsx', index=False, header=True, columns=["Tweet", "Preprocesing", "Translate", "Labeling"])