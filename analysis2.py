import pandas as pd
from googletrans import Translator

data = pd.read_excel('data/data_analisis2.xlsx')
df = pd.DataFrame(data)

tweet_positif = 0
tweet_netral = 0
tweet_negatif = 0

for label in df['Labeling'] :
    if label == "positif" : 
        tweet_positif += 1
    elif label == "netral" :
        tweet_netral += 1
    else :
        tweet_negatif += 1

df['Tweet_clean'] = df['Preprocesing']

def set_sentiment (text) :
    if text == "positif" :
        return 1
    elif text == "netral" : 
        return 0 
    else :
        return -1

df['Sentiment'] = df['Labeling'].apply(set_sentiment)

# print('positif ', tweet_positif/len(df)*100)
# print('netral ', tweet_netral/len(df)*100)
# print('negatif ', tweet_negatif/len(df)*100)

df.to_excel('data/data_analisis3.xlsx', index=False, header=True, columns=["Tweet", "Tweet_clean", "Sentiment"])