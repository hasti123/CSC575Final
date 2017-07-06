#!/usr/bin/env python

"""main.py - Aaron Hunter. This is the entry point to the Tweet processing and query system."""

from lib import term_index
from lib import tf_idf_index
from lib import query
from lib import tweet_processor

print('Init inverted index.')
termIndex = term_index.TermIndex()

print('Init TFxIDF index.')
tfIdfIndex = tf_idf_index.TFIDFIndex()

print('Processing new teweets.')
tweetProc = tweet_processor.TweetProcessor(termIndex)
hasNewTweets = tweetProc.processTweets()

if hasNewTweets:
  print('Recomputing IDF values')
  termIndex.computeIDF()

  print('Saving the updated index.')
  termIndex.saveIndex()

  print('Recomputing TFxIDF index.')
  tfIdfIndex.recompute(termIndex) 
  tfIdfIndex.saveIndex()
  print('Saving the updated index.')

  tfIdfIndex.printIndex()
  termIndex.printIndex()

maxTweets = input('Enter the maximum number of tweets to return (default 5):')
if not maxTweets.isdigit():
  print('That was not a number. Using 5.')
  maxTweets = 5

print('Ready')

def run():
  q = input('Enter your query: ')
  print('Searching...')
  qproc = query.Query()
  documents = qproc.executeQuery(q, termIndex, tfIdfIndex, int(maxTweets))
  if len(documents) == 0:
    print('Nothing found...')
  else:
    print("### RESULTS ###")
    print("## " + str(len(documents)) + " tweets returned ##")
  for d in documents:
    print("### TWEET DETAILS ###")
    print('File Name: ' + d.fileName)
    print('Twitter Account: ' + d.twitterAccount)
    print('Timestamp: ' + str(d.timestamp))
    print('Content: ' + d.originalContent)
    print(' ')
  run()
run()
