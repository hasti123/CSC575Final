#!/usr/bin/env python

"""inverted_index.py - Aaron Hunter. This is a utility class for managing
   inverted indexes, sotred on disk."""

import os
import pickle
import pprint

class InvertedIndex:
    __indexDir = 'index'

    def __init__(self, indexFile):
        self.__indexFile = indexFile
        self.invertedIndex = {}

    def getIndex(self):
      return self.invertedIndex

    def hasTerm(self, term):
        return term in self.invertedIndex

    def printIndex(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(self.invertedIndex)

    def __loadIndex__(self):
      if (os.path.exists(self.__invertedIndexPath())):
        self.invertedIndex = pickle.load(open(self.__invertedIndexPath(), 'rb'));

    def __invertedIndexPath(self):
      return os.path.join(self.__indexDir, self.__indexFile)

    def saveIndex(self):
      pickle.dump(self.invertedIndex, open(self.__invertedIndexPath(), 'wb'));

    def countDocuments(self):
        docSet = set()
        for k,v in self.invertedIndex.items():
            for d in v['documents']:
                docSet.add(d)
        return len(docSet)
