#!/usr/bin/env python

"""term_index.py - Aaron Hunter. An index to represent the TFxIDF values
   for terms in indexed documents. Generally used for retrieval ranking."""

from . import document
from . import inverted_index
from . import term_index

class TFIDFIndex(inverted_index.InvertedIndex):
  __indexFile = 'tf_idf_index.pickle'

  def __init__(self):
    super().__init__(self.__indexFile)
    super().__loadIndex__()

  def recompute(self, termIndex):
    for term,v in termIndex.getIndex().items():
      documents = termIndex.getDocuments(term)
      for d in documents:
        if term not in self.invertedIndex:
          self.invertedIndex[term] = {}
        self.invertedIndex[term][d.uuid] = {'raw': 0, 'tfidf': 0}
        self.invertedIndex[term][d.uuid]['raw'] = d.terms[term]
        self.invertedIndex[term][d.uuid]['tfidf'] = d.terms[term]['tf'] * v['idf']
