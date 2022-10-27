from cmath import log
import pandas as pd
from textblob import TextBlob

data = pd.read_excel('data/data_preprocesing3.xlsx')
df = pd.DataFrame(data).head(1000)

def text_blob (text) :
    x = TextBlob(text)
    return x.sentiment.polarity

df['Sentimen'] = df['Preprocesing'].apply(text_blob)

def labeling (sentiment) :
    if sentiment > 0.0 :
        return "POSITIF"
    elif sentiment == 0.0 :
        return "NETRAL"
    else :
        return "NEGATIF"

df['Label'] = df['Sentimen'].apply(labeling)

# print(df)
print([element for element in df['Label'] if element == "NETRAL"])
# df.to_excel('data/data_analisis.xlsx')
quit()

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
