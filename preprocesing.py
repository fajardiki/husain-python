import pandas as pd

import string
import re

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# import nltk
# nltk.download('punkt')

data = pd.read_excel('export_data_tweet_all.xlsx')
df = pd.DataFrame(data).head(10)

# CASE FOLDING
df['Tweet'] = df['Tweet'].str.lower()

# TOKENIZING
def remove_tweet_special(text):
    # remove tab, new line, ans back slice
    text = text.replace('\\t'," ").replace('\\n'," ").replace('\\u'," ").replace('\\',"")
    # remove non ASCII (emoticon, chinese word, .etc)
    text = text.encode('ascii', 'replace').decode('ascii')
    # remove mention, link, hashtag
    text = ' '.join(re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)"," ", text).split())
    # remove incomplete URL
    return text.replace("http://", " ").replace("https://", " ")

df['Tweet'] = df['Tweet'].apply(remove_tweet_special)

#remove number
def remove_number(text):
    return  re.sub(r"\d+", "", text)

df['Tweet'] = df['Tweet'].apply(remove_number)

#remove punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans("","",string.punctuation))

df['Tweet'] = df['Tweet'].apply(remove_punctuation)

#remove whitespace leading & trailing
def remove_whitespace_LT(text):
    return text.strip()

df['Tweet'] = df['Tweet'].apply(remove_whitespace_LT)

#remove multiple whitespace into single whitespace
def remove_whitespace_multiple(text):
    return re.sub('\s+',' ',text)

df['Tweet'] = df['Tweet'].apply(remove_whitespace_multiple)

# remove single char
def remove_singl_char(text):
    return re.sub(r"\b[a-zA-Z]\b", "", text)

df['Tweet'] = df['Tweet'].apply(remove_singl_char)

# NLTK word Tokenize 
def word_tokenize_wrapper(text):
    return word_tokenize(text)

df['Tweet Tokens'] = df['Tweet'].apply(word_tokenize_wrapper)

# df.to_excel('data_tokenizing_tes.xlsx')
print(df)