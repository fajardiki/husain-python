import pandas as pd
from textblob import TextBlob
from googletrans import Translator

data = pd.read_excel('data/data_preprocesing3.xlsx')
df = pd.DataFrame(data)

translator = Translator()

def textblob_translate (text) :
    translation = translator.translate(text, src="id", dest="en")
    return translation.text

df['Translate'] = df['Preprocesing'].apply(textblob_translate)

# def fit_stopword(text) : 
#     return text.replace(',',"")
# df['Translate'] = df['Translate'].apply(lambda x: fit_stopword(x))

def sentiment_polarity (text) : 
    if TextBlob(text).sentiment.polarity > 0.0 :
        return "positif"
    elif TextBlob(text).sentiment.polarity == 0.0 :
        return "netral"
    else : 
        return "negatif"

df['Labeling'] = df['Translate'].apply(sentiment_polarity)

df.to_excel('data/data_analisis.xlsx')
