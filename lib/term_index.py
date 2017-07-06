#!/usr/bin/env python

"""term_index.py - Aaron Hunter. An index to represent terms and IDF
   for documents documents. Generally used for initial keyword retrieval"""

from . import document
from . import inverted_index

import json
import math
import os
import pickle

class TermIndex(inverted_index.InvertedIndex):
  __indexFile = 'raw_term_index.pickle'

  def __init__(self):
    super().__init__(self.__indexFile)
    super().__loadIndex__()

  def appendIndex(self, term, freq, doc):
    if not self.hasTerm(term):
      self.invertedIndex[term] = {'freq': 0, 'documents': []}
    self.invertedIndex[term]['freq'] += freq
    self.invertedIndex[term]['documents'].append(doc.uuid)

  def processStemDictionary(self, doc):
    for k, v in doc.terms.items():
      self.appendIndex(k, v['count'], doc)

  def getDocuments(self, term):
    documentList = []
    for d in self.invertedIndex[term]['documents']:
      documentList.append(pickle.load(open(os.path.join('document_objs', d + '.docobj'), 'rb')))
    return documentList

  #IDF(t) = log_e(Total number of documents / Number of documents with term t in it)
  def computeIDF(self):
    docCount = self.countDocuments()
    for k,v in self.invertedIndex.items():
      idf = math.log(docCount / len(v['documents']))
      v['idf'] = idf

  def getFreq(self, term):
    return self.invertedIndex[term]['freq']
