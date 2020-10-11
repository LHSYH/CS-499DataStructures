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
#set Up URI paths for REST service

@route('/delete', method='GET')
def delete():
  id=request.query.id
  findJson={"id":id}
  return delete_document(findJson)

def delete_document(findDocument):
  try:
    result=collection.remove(findDocument)
  except Exception as ve:
    print 'Exception handled: ', ve
    
if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)