#!/usr/bin/env python

"""document_service.py - Charlie Hastings, writes a tweet to a tweet document"""

import sys
import uuid
from tweet import *
import json
import os.path

def writeTweetToDocument(tweet):
    writeToDocument(json.dumps(tweet.__dict__))

def writeToDocument(value):
    filename = str(uuid.uuid1()) + '.tweet'
    save_path = "../intake/"
    fullfilename = os.path.join(save_path, filename)
    outputFile = open(fullfilename, 'w')
    outputFile.write(value)
    outputFile.close()
