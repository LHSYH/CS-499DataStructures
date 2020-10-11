#!/usr/bin/python
import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def read_document(industry):
    try:
        findDocument = {"Industry":industry}
        result=collection.find(findDocument,{"Ticker":1,"_id":0})
        print(json_util.dumps(list(result)))
    except ValidationError as ve:
        abort(400, str(ve))
        return False
    else:
        return True
      
def main():
    read_document("Medical Laboratories & Research")

main()
