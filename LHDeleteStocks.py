#!/usr/bin/python
import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def delete_document(findDocument):
    try:
        result=collection.remove(findDocument)
        print(json_util.dumps(list(result)))
    except ValidationError as ve:
        abort(400, str(ve))
        print 'Exception handled:', ve
        
def main():
    findDocument = {"Ticker":"BRLI"}
    print delete_document(findDocument)
    print "Deletion confirmed"

main()
