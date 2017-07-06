#!/usr/bin/env python

"""tweet.py - Charlie Hastings an object to hold tweet properties"""

class Tweet:
    def __init__(self, timestamp, account, content, relevancy=""):
        self.timestamp = timestamp
        self.account = account
        self.content = content
        self.relevancy = relevancy
