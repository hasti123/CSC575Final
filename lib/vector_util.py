#!/usr/bin/env python

"""vector_util.py - Aaron Hunter. Used to experiment with different TF
   normalization algorithms via the defaultTF interface."""

#defaultTF can be modified to change the term normalization algorithm for the system.
def defaultTF(termVector):
  return booleanTF(termVector)

# Due to the fact that Tweets are very short, we've opted for the boolean TF normalization scheme.
# http://nlp.stanford.edu/IR-book/html/htmledition/document-and-query-weighting-schemes-1.html#sec:querydocweighting
def booleanTF(termVector):
  booleanTermVector = {}
  for term,termDict in termVector.items():
    booleanTermVector[term] = termDict
    if termDict['count'] >= 1:
      booleanTermVector[term]['tf'] = 1
    else:
      booleanTermVector[term]['tf'] = 0
  return booleanTermVector
