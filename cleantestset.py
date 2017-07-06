#!/usr/bin/env python

"""cleantestset.py - Charlie Hastings, remove duplicates from test set"""

import codecs
import glob
import json
import os
import pickle
import shutil
from lib import document

documents = []

__fileDir = 'test_set/$GOOG'

def processTweets():
    newFileCount = 0
    result_documents = []
    for file in glob.glob(os.path.join(__fileDir, '*.tweet')):
        result_documents.append(__processFile(file))
    return result_documents

def __processFile(file):
    f = codecs.open(file, 'r', 'UTF-8')
    fileContent = json.load(f)
    return document.Document(fileContent)

#Possibly want to group/remove duplicates?
def remove_duplicates(documents):
    tweet_count = 0
    results = []
    duplicates = []
    for document in documents:
        if has_duplicate(document, results):
            duplicates.append(document)
        else:
            results.append(document)
    return duplicates

def has_duplicate(document, results):
    for result in results:
        if document.originalContent == result.originalContent:
            return True
    return False


documents = processTweets()
dupes = remove_duplicates(documents)

for dupe in dupes:
    print(dupe.originalContent)
