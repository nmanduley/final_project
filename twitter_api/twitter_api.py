import tweepy
import configparser
import os
import pandas as pd

# Read configs
config = configparser.ConfigParser()
filepath = os.path.normpath(os.getcwd() + '/twitter_api/config.ini')
config.read(filepath)

api_key = config['twitter']['API_KEY']
api_key_secret = config['twitter']['API_KEY_SECRET']
access_token = config['twitter']['ACCESS_TOKEN']
access_token_secret = config['twitter']['ACCESS_TOKEN_SECRET']

# Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search tweets
hashtags = ['#stocks', '#stocksmarket']
keywords = ['Amazon', 'AMZN']
search_criteria = hashtags+keywords
limit = 10

tweets = tweepy.Cursor(api.search_tweets,\
    q=search_criteria,
    count=10,
    tweet_mode='extended').items(limit)

# Create dataframe 
columns = ['Time', 'User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
df.head()