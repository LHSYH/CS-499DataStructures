#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, abort
import datetime
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# set up URI paths for REST service
@route('/create', method='POST')
def post_create():
  strings=request.json
  print insert_document(strings)

def insert_document(document):
  try:
    result=collection.insert(document)
  except Exception as ve:
      return True
  else:
      return False

if __name__ == '__main__':
 #app.run(debug=True)
 run(host='localhost', port=8080)