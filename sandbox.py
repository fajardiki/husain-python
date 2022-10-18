import pandas as pd
from ast import literal_eval


# ...........................................................................
#### UNTUK MENDAPATKAN KATA PER KATA HASIL TOKENIZING, UNTUK NORMALISASI KATA

data = pd.read_excel('data/data_preprocesing2.xlsx')
df = pd.DataFrame(data)
df['Stemmer'] = df['Stemmer'].apply(literal_eval)

word = []
for data in df['Stemmer']:
    for tokenize in data:
        word.append(tokenize)

word_data = pd.DataFrame(word)
word_data.to_excel('data/data_word.xlsx', index=False, header=True)

# ....................................................................
#### SASTRAWI ADALAH UNTUK STEMMING, YAITU MENGUBAH KATA KE KATA DASAR

# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# factory = StemmerFactory()
# stemmer = factory.create_stemmer()

# # stemming proses
# sentence = 'Perkembangan kuliner di indonesia cukup membanggakan dalam 10 tahun terakhir'
# output = stemmer.stem(sentence)

# print(output)