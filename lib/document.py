#!/usr/bin/env python

"""document.py - Aaron Hunter. Represents processed tweets, as well as metadata
   , and persistence information."""

from . import stemmer
from . import stopword
from . import vector_util

import os
import pickle
import uuid

#Returns an instance of Document for the given ID.
def loadDocument(documentId):
  return pickle.load(open(os.path.join('document_objs', documentId + ".docobj"), 'rb'))

class Document:
  def __init__(self, fileContent):
    self.uuid = str(uuid.uuid4())
    self.folder = "document_objs"
    self.fileName =  self.uuid + '.docobj'
    self.twitterAccount = fileContent['account']
    self.timestamp = fileContent['timestamp']
    self.originalContent = fileContent['content']
    self.termCount = 0
    self.terms = {}

  def addTerms(self):
    words = stemmer.getStemDictionary(stopword.removeStopWords(self.originalContent))
    for w,count in words.items():
      if w not in self.terms:
        self.terms[w] = {}
      self.terms[w]['count'] = count
    self.termCount = len(self.terms)

  def computeTF(self):
    self.terms = vector_util.defaultTF(self.terms)

  def save(self):
    pickle.dump(self, open(os.path.join(self.folder, str(self.fileName)), 'wb'))
