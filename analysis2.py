import pandas as pd

data = pd.read_excel('data/data_analisis.xlsx')
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

print(tweet_positif/len(df)*100)
print(tweet_netral/len(df)*100)
print(tweet_negatif/len(df)*100)

# df.to_excel('data/data_analisis2.xlsx')