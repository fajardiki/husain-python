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
import matplotlib.pyplot as plt
import numpy as np

from ast import literal_eval

# post_list = open("kata_positif.txt", "r")
# post_kata = post_list.readlines()
# neg_list = open("kata_negatif.txt", "r")
# neg_kata = neg_list.readlines()

# df = pd.DataFrame(post_kata)
# print(df)
sentiments = []

preprocesing_data = pd.read_csv('data_tokenizing_tes.csv')
data_positif_negatif = pd.read_excel('kata-positif-negatif.xlsx')

pos_kata = pd.DataFrame(data_positif_negatif, columns=["positif"]).dropna()
neg_kata = pd.DataFrame(data_positif_negatif, columns=["negatif"]).dropna()

data_tweets = pd.DataFrame(preprocesing_data, columns=['Tweet Tokens WSW'])
data_tweets['Tweet Tokens WSW'] = data_tweets['Tweet Tokens WSW'].apply(literal_eval)

jumlah_kata = 0
jml_kata_positif = 0
jml_kata_negatif = 0
probabilitas_positif = 0
probabilitas_negatif = 0

for items in data_tweets['Tweet Tokens WSW'] :
    # print(items)
    count_p = 0 #nilai positif
    count_n = 0 #nilai negatif

    for tweet in items : 
        jumlah_kata += 1
        # print(tweet)
        for kata_pos in pos_kata['positif'] :
            # print(kata_pos)
            if (kata_pos == tweet) :
                count_p += 1 
        for kata_neg in neg_kata['negatif'] :
            # print(kata_pos)
            if (kata_neg == tweet) :
                count_n += 1

    # print("positif : " + str(count_p))
    # print("negatif : " + str(count_n))
    sentiments.append(count_p - count_n)
    jml_kata_positif += count_p
    jml_kata_negatif += count_n

# print(sentiments)
print("jumlah kata : " + str(jumlah_kata))
print("kata positif : " + str(jml_kata_positif))
print("kata negatif : " + str(jml_kata_negatif))