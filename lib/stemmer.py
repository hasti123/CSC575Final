#!/usr/bin/env python

"""stemmer.py - Aaron Hunter. Wrapper for the external Porters Stemming
   algorithm. Used to stem lists, or individual words."""

from lib.external import porters

def getStemDictionary(wordList):
    stemDict = {}
    for word in wordList:
        stem = stemWord(word)
        if stem in stemDict:
            stemDict[stem] += 1
        else:
            stemDict[stem] = 1
    return stemDict

def stemWord(word):
  p = porters.PorterStemmer()
  word = word.lower()
  return p.stem(word, 0, len(word)-1)

