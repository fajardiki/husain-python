import pandas as pd

import string
import re

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

data = pd.read_excel('export_data_tweet_all.xlsx')
df = pd.DataFrame(data)

# CASE FOLDING
df['Tweet'] = df['Tweet'].str.lower()

# TOKENIZING
def remove_tweet_special(text):
    text = text.replace('\\t'," ").replace('\\n'," ").replace('\\u'," ").replace('\\',"")
    text = text.encode('ascii', 'replace').decode('ascii')
    text = ' '.join(re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)"," ", text).split())
    return text.replace("http://", " ").replace("https://", " ")

df['Tweet'] = df['Tweet'].apply(remove_tweet_special)

def remove_number(text):
    return  re.sub(r"\d+", "", text)

df['Tweet'] = df['Tweet'].apply(remove_number)

def remove_punctuation(text):
    return text.translate(str.maketrans("","",string.punctuation))

df['Tweet'] = df['Tweet'].apply(remove_punctuation)

def remove_whitespace_LT(text):
    return text.strip()

df['Tweet'] = df['Tweet'].apply(remove_whitespace_LT)

def remove_whitespace_multiple(text):
    return re.sub('\s+',' ',text)

df['Tweet'] = df['Tweet'].apply(remove_whitespace_multiple)

def remove_singl_char(text):
    return re.sub(r"\b[a-zA-Z]\b", "", text)

df['Tweet'] = df['Tweet'].apply(remove_singl_char)

def word_tokenize_wrapper(text):
    return word_tokenize(text)

df['Tweet Tokens'] = df['Tweet'].apply(word_tokenize_wrapper)


# FILTERING (STOPWORD REMOVAL)

list_stopwords = stopwords.words('indonesian')

# list_stopwords.extend(["yg", "dg", "rt", "dgn", "ny", "d", 'klo', 
#                        'kalo', 'amp', 'biar', 'bikin', 'bilang', 
#                        'gak', 'ga', 'krn', 'nya', 'nih', 'sih', 
#                        'si', 'tau', 'tdk', 'tuh', 'utk', 'ya', 
#                        'jd', 'jgn', 'sdh', 'aja', 'n', 't', 
#                        'nyg', 'hehe', 'pen', 'u', 'nan', 'loh', 'rt',
#                        '&amp', 'yah'])
# convert list to dictionary
list_stopwords = set(list_stopwords)

#remove stopword pada list token
def stopwords_removal(words):
    return [word for word in words if word not in list_stopwords]

df['Tweet Tokens WSW'] = df['Tweet Tokens'].apply(stopwords_removal)

# CONVERT NEGATION / NORMALIZATION
# skip wkwk :D

df.to_excel('data_tokenizing_tes.xlsx')
