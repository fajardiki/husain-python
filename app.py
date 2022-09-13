import snscrape.modules.twitter as nstwitter
import pandas as pd

data_container = []

for i, tweet in enumerate(nstwitter.TwitterSearchScraper('#esport').get_items()) :
    if i > 100 :
        break
    data_container.append([tweet.date, tweet.rawContent, tweet.likeCount, tweet.quoteCount])

data_pd = pd.DataFrame(data_container, columns=["Date Tweet", "Tweet", "Count of Likes", "Count of quote"])
data_pd['Date Tweet'] = pd.to_datetime(data_pd['Date Tweet'])

# print(data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx', ))
data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx', index=False, header=True)