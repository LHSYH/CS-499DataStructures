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

@route('/update', method='GET')
def update():
  id=request.query.id
  result=request.query.result
  findJson={"id":id}
  updateJson={"result":result}
  return update_document(findJson, updateJson)

def update_document(findDocument, newDocument):
  try:
    result=collection.update(findDocument, {"$set": newDocument})
  except Exception as ve:
      return False

if __name__ == '__main__':
 #app.run(debug=True)
 run(host='localhost', port=8080)