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

@route('/summarystocks', method='GET')
def get_summarystocks():
    tickers=request.query.tickers
    #tickers=['A','TP']
    print(tickers)
    tickers=tickers.split(",")  
    findStr={"Ticker":{"$in":tickers}}
    return read_document(findStr)
    
    
def read_document(document):
    try:
        result=collection.find(document)
        return (json_util.dumps(list(result)))
    except Exception as ve:
        abort(400, str(ve))
        return False
    else:
        return True


if __name__ == '__main__':
	#app.run(debug=True)
	run(host='localhost', port=8085)
