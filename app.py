import snscrape.modules.twitter as nstwitter
import pandas as pd

data_container = []

for i, tweet in enumerate(nstwitter.TwitterSearchScraper('#esport lang:id').get_items()) :
    if i > 3000 :
        break
    data_container.append([
        tweet.rawContent,
        tweet.renderedContent,
        tweet.id,
        tweet.user,
        tweet.replyCount,
        tweet.retweetCount,
        tweet.likeCount,
        tweet.quoteCount,
        tweet.conversationId,
        tweet.lang,
        tweet.source
    ])

data_pd = pd.DataFrame(data_container, columns=[
    "rawContent",
    "renderedContent",
    "id",
    "user",
    "replyCount",
    "retweetCount",
    "likeCount",
    "quoteCount",
    "conversationId",
    "lang",
    "source"
])

# print(data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx'))
data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx', index=False, header=True)