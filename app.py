import snscrape.modules.twitter as nstwitter
import pandas as pd

data_container = []

for i, tweet in enumerate(nstwitter.TwitterSearchScraper('esport indonesia lang:in').get_items()) :
    # if i > 5000 :
    #     break
    data_container.append([tweet.rawContent])
    # data_container.append([tweet.rawContent, tweet.user, tweet.hashtags, tweet.lang, tweet.date])

data_pd = pd.DataFrame(data_container, columns=["Tweet"])
# data_pd = pd.DataFrame(data_container, columns=["Tweet", "User", "Hastag", "Bahasa", "Tanggal"])
# data_pd['Tanggal'] = data_pd['Tanggal'].apply(lambda a: pd.to_datetime(a).date())

# print(data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx', ))
# data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx', index=False, header=True)
# data_pd.to_excel(r'D:\FREELANCE\husain-python\export_data_tweet_all.xlsx', index=False, header=True)
data_pd.to_csv(r'D:\FREELANCE\husain-python\export_data_tweet_all.xlsx', index=False, header=True)
