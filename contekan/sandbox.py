import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from nltk.corpus import stopwords 
from ast import literal_eval 

data = pd.read_excel('data-example/data_preprocesing3.xlsx')
df = pd.DataFrame(data)
comment_words = ""

for val in df.Preprocesing : 
    comment_words += val 

list_stopwords = stopwords.words('indonesian')

list_stopwords = set(list_stopwords)

wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=list_stopwords, min_font_size=10).generate(comment_words)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()


quit()

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