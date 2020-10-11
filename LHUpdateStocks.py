#!/usr/bin/python
import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def update_document(findDocument, newDocument):
    try:
        result=collection.update(findDocument,{"$set":newDocument})
        print(json_util.dumps(list(result)))
    except ValidationError as ve:
        abort(400, str(ve))
        print 'Exception handled:', ve
        return False
      
def main():
    findDocument = {"Ticker":"TP","Volume":1247858}
    newDocument = {"Ticker":"TP","Volume":16000}
    print update_document(findDocument,newDocument)
    print(findDocument, newDocument)

main()
