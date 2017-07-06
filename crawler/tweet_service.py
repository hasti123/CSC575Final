#!/usr/bin/env python

"""tweet_service.py - Tweets a message out to the given account"""

import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
def tweet(message):
    api.update_status(message)
    time.sleep(15) # Sleep for 15 seconds to control spamming of account

