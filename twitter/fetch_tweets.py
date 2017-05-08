import tweepy
from tweepy import OAuthHandler
import json

from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

with open('tweets.json', 'w') as json_file:
    page = 1
    counter = 0
    while True:
        tweets =api.user_timeline(id="taylorswift13",count=300,page=page)

        if tweets:
            for tweet in tweets:
                json_tweet = tweet._json
                json_file.write(json.dumps(json_tweet))
                json_file.write("\n")
                counter+=1
                if counter==300:
                    exit()
        else:
            break
        page += 1

