import tweepy
import pandas as pd

# client = tweepy.Client(
#     consumer_key='LUCuFYWflBqslJQwIoM6l5Dfa', 
#     consumer_secret='gRRaNKWbKU1ARYLrl8hTb9pJR1bSvKFsMZldQkQ47UAdHE65ry',
#     access_token='1576425288551960576-17kzcAhJGrwRdALwgZummmgLrexZSp', 
#     access_token_secret='Q3PqRgxI7NKQHvE6K9nvk6MoFLkGWNtomxvsJsl78PLpW'
# )

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAK%2FdhgEAAAAAZADNVdLLc%2BnrmOXn6Io16jvRW8s%3DdtTkJjWNU6BHGgFAMZgVniSmzqMqKAmjRX9i8LnGEnn7AtSSbO')

tweets = client.search_recent_tweets(query='esport lang:id', max_results=200)

df = pd.DataFrame(tweets.data, columns=['text'])
df.to_excel('crawling_data_tweets.xlsx')

# print(tweets)
# for tweet in tweets.data:
#     print(tweet.text)