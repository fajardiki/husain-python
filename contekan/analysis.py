import pandas as pd
from textblob import TextBlob
from googletrans import Translator
from deep_translator import GoogleTranslator

# translator = GoogleTranslator(source="id", target="en")

data = pd.read_excel('data/data_analisis.xlsx')
df = pd.DataFrame(data)

def sentiment_polarity (text) : 
    if TextBlob(text).sentiment.polarity > 0.0 :
        return "positif"
    elif TextBlob(text).sentiment.polarity == 0.0 :
        return "netral"
    else : 
        return "negatif"

df['Labeling'] = df['Translate'].apply(sentiment_polarity)

df.to_excel('data/data_sentiment.xlsx', index=False, header=True, columns=["Tweet", "Preprocesing", "Translate", "Labeling"])