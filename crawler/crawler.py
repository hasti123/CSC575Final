#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""crawler.py - Charlie Hastings grabs tweets for a given stock name and writes them to a doc"""

import time
import tweepy
from tweet_service import api
from document_service import writeTweetToDocument
from tweet import Tweet

# this is the function that does most of the work of the bot
def run_crawler(stock_name, number_of_items):
    """Runs twitter crawler"""
    result = tweepy.Cursor(api.search, q=stock_name).items(number_of_items)

    for status in result:
        new_tweet = Tweet(time.mktime(status.created_at.timetuple()), status.user.screen_name, status.text)
        writeTweetToDocument(new_tweet)

def run_relevancy_crawler(stock_name, number_of_items):
    """Runs twitter crawler with user input for relevancy"""
    result = tweepy.Cursor(api.search, q=stock_name).items(number_of_items)

    for status in result:
        print(status.text)
        relevancy = raw_input()
        new_tweet = Tweet(time.mktime(status.created_at.timetuple()), status.user.screen_name, status.text, relevancy)
        writeTweetToDocument(new_tweet)
