#!/usr/bin/env python

"""tweet_processor.py - Aaron Hunter. The tweet processor is responsible for
   processing all tweets in the intake folder, and generating document
   objects for them. The term_index is updated for new documents. The
   recomputation of IDF and the TFxIDF index is done separately to reduce
   load."""

from lib import document

import codecs
import glob
import json
import os
import pickle
import shutil

class TweetProcessor:
    __fileDir = 'intake'
    __termIndex = {}

    def __init__(self, termIndex):
      self.__termIndex = termIndex

    def processTweets(self):
      newFileCount = 0
      for file in glob.glob(os.path.join(self.__fileDir, '*.tweet')):
        self.__processFile(file)
        newFileCount += 1
      return newFileCount > 0

    def __processFile(self, file):
      f = codecs.open(file, 'r', 'UTF-8')
      fileContent = json.load(f)
      newDocument = document.Document(fileContent)
      newDocument.addTerms()
      newDocument.computeTF()
      self.__termIndex.processStemDictionary(newDocument)
      newDocument.save()
      shutil.move(file, os.path.join('processed', str(newDocument.fileName)))
