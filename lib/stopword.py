#!/usr/bin/env python

"""stopword.py - Aaron Hunter. The NTLK stop words and tokenziation libraries
   are used to avoid creating our own corpus.
   See https://pythonspot.com/nltk-stop-words/ for more information on the
   NTLK toolkit."""

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import nltk
import os
import re

#Removes stopWords unless they happen to be a ticker symbol.
def removeStopWords(text):
  dir = os.path.dirname(__file__)
  nltk.data.path.append(os.path.join(dir, 'nltk_data'))

  tickerRegex = re.compile('\$(?:[A-Za-z])+')
  wordRegex = re.compile('(?:[A-Za-z0-9#.-])+')
  hashtagRegex = re.compile('#(?:[A-Za-z0-9])+')
  stopWords = set(stopwords.words('english'))

  wordsFiltered = []

  #Pull any ticker symbols out of the text.
  newText = ''
  for word in text.split():
    if tickerRegex.match(word): wordsFiltered.append(word.lower())
    else:
      if hashtagRegex.match(word): wordsFiltered.append(word.lower().replace('#', ''))
      else:
        if wordRegex.match(word): newText += word + ' '

  #We can tokenize now.
  for word in nltk.word_tokenize(newText):
    if word not in stopWords:
      wordsFiltered.append(word)

  return wordsFiltered
