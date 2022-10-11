import snscrape.modules.twitter as nstwitter
import pandas as pd

data_container = []

for i, tweet in enumerate(nstwitter.TwitterSearchScraper(query="esport OR esport_indonesia OR esportindonesia OR #esport OR #esports OR #esport_indonesia OR #esportindonesia lang:id").get_items()) :
    if i > 1000 :
        break
    data_container.append([tweet.rawContent, tweet.hashtags, tweet.lang])
    # data_container.append([tweet.rawContent, tweet.user, tweet.hashtags, tweet.lang, tweet.date])

data_pd = pd.DataFrame(data_container, columns=["Tweet", "hashtags", "lang"])
# data_pd = pd.DataFrame(data_container, columns=["Tweet", "User", "Hastag", "Bahasa", "Tanggal"])
# data_pd['Tanggal'] = data_pd['Tanggal'].apply(lambda a: pd.to_datetime(a).date())

# print(data_pd.to_excel(r'C:\Users\ASUS\Documents\export_data_tweet.xlsx', ))
# data_pd.to_excel(r'E:\FREELANCE\FREELANCE-TA-HUSAIN-PYTHON\export_data_tweet.xlsx', index=False, header=True)
data_pd.to_excel('data\data_tweet.xlsx', index=False, header=True)
# data_pd.to_excel(r'E:\FREELANCE\FREELANCE-TA-HUSAIN-PYTHON\data_tweet.csv', index=False, header=True)
