import snscrape.modules.twitter as nstwitter
import pandas as pd

data_container = []

for i, tweet in enumerate(nstwitter.TwitterSearchScraper("esport OR esport_indonesia OR esportindonesia OR #esport OR #esports OR #esport_indonesia OR #esportindonesia lang:id since:2021-11-06 until:2021-11-13").get_items()) :
    if i > 500 :
        break
    data_container.append([tweet.rawContent, tweet.hashtags, tweet.date, tweet.lang])

data_pd = pd.DataFrame(data_container, columns=["Tweet", "hashtags", "date", "lang"])
data_pd.to_excel('data\data_tweet.xlsx', index=False, header=True)