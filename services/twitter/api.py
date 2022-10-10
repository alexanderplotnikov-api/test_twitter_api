import tweepy
import os

auth = tweepy.OAuthHandler(os.environ.get('TWITTER_API_KEY'),os.environ.get('TWITTER_API_SECRET_KEY'))
auth.set_access_token(os.environ.get('TWITTER_API_ACCESS_TOKEN'),os.environ.get('TWITTER_API_ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)