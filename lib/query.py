#!/usr/bin/env python

"""query.py - Aaron Hunter. Retrieves documents matching stemmsed query
   keywords from the term_index. Then, The TFxIDF index is used to
   compute cosine similarity, then document objects are returned in descending
   order of cosine similarity."""

from . import vector_util
from . import stemmer
from . import stopword
from . import document

import math
import os

class Query:
  #Returns the documents for a particular query.
  def executeQuery(self, query, termIndex, tfIdfIndex, maxTweets):
    qVector = Query.getQueryVector(stopword.removeStopWords(query))
    documentDict = Query.getDocuments(termIndex, qVector.keys())
    return Query.removeDuplicates(Query.cosineSimRank(termIndex, tfIdfIndex, qVector, documentDict), maxTweets)

  def hasDuplicate(document, results):
    for result in results:
      if document.originalContent == result.originalContent: return True
    return False

  #Possibly want to group/remove duplicates?
  def removeDuplicates(documents, maxTweets):
    tweetCount = 0
    results = []
    for document in documents: 
      if Query.hasDuplicate(document, results):
          continue
      tweetCount += 1
      if tweetCount > maxTweets: return results
      results.append(document)
    return results

  def getDocuments(termIndex, qList):
    documents = {}
    for q in qList:
      if not termIndex.hasTerm(q):
        continue
      documentList = termIndex.getDocuments(q) 
      for d in documentList:
        if q not in documents:
          documents[q] = []
        documents[q].append(d)
    return documents

  def getQueryVector(queryList):
    qVector = {}
    for q in queryList:
      qStem = stemmer.stemWord(q)
      if qStem not in qVector:
        qVector[qStem] = {'count': 0}
      qVector[qStem]['count'] += 1
    return qVector


  def cosineSimRank(termIndex, tfIdfIndex, qVector, documents):
    cosineDict = {'query': {}, 'documents': {}}
    #Normalize the query vector term frequencies.
    qVector = vector_util.defaultTF(qVector)

    termDict = termIndex.getIndex()
    tfIdfDict = tfIdfIndex.getIndex()

    #Convert the query vector into TFxIDF values.
    tempQVector = {}
    queryCosineDict = cosineDict['query']
    for term,queryDict in qVector.items():
      tempQVector[term] = queryDict
      if term not in termDict:
        continue
      tfidf = queryDict['tf'] * termDict[term]['idf']
      tempQVector[term]['tfidf'] = tfidf
      if term not in queryCosineDict:
        queryCosineDict[term] = 0
      queryCosineDict[term] += tfidf**2
    qVector = tempQVector

    #Create the document-tfxidf vectors for the retrieved documents.
    documentVector = {}
    for term, documentList in documents.items():
      for doc in documentList:
        if doc.uuid not in documentVector:
          documentVector[doc.uuid] = {}
        for term in doc.terms:
          documentDict = documentVector[doc.uuid]
          if term not in documentDict:
            documentDict[term] = tfIdfDict[term][doc.uuid]['tfidf']

    cosineDocDict = cosineDict['documents']
    for uuid, documentDict in documentVector.items():
      cosineDocDict[uuid] = {'numerator_dot_product': 0, 'vector_square': 0}
      numeratorProduct = 0
      for term, tfidf in documentDict.items():
        cosineDocDict[uuid]['vector_square'] += tfidf**2
        if term not in qVector:
          continue
        numeratorProduct += qVector[term]['tfidf'] * tfidf
        cosineDocDict[uuid]['numerator_dot_product'] = numeratorProduct
      cosineDocDict[uuid]['vector_square'] = math.sqrt(cosineDocDict[uuid]['vector_square'])

    #Create the cosine similarity value for each query.
    queryVectorSqrt = 0
    for term, tfidfsq in queryCosineDict.items():
      queryVectorSqrt += tfidfsq
    queryVectorSqrt = math.sqrt(queryVectorSqrt)

    #Finally get the values
    docSums = {}
    for uuid, value in cosineDocDict.items():
      numeratorDotProduct = value['numerator_dot_product']
      if numeratorDotProduct == 0:
        continue
      docSums[uuid] = cosineDocDict[uuid]['numerator_dot_product'] / (cosineDocDict[uuid]['vector_square'] * queryVectorSqrt)

    rankedDict = {}
    for uuid, cosineSim in docSums.items():
      if cosineSim not in rankedDict:
        rankedDict[cosineSim] = []
      rankedDict[cosineSim].append(uuid)

    rankKeys = reversed(sorted(rankedDict.keys()))
    documentList = []
    for key in rankKeys:
      for documentId in rankedDict[key]:
        documentList.append(document.loadDocument(documentId))
    return documentList

