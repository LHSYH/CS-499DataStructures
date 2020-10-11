#!/usr/bin/python
import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


def insert_document(document):
    try:
        result=collection.insert(document)
    except ValidationError as ve:
        abort(400, str(ve))
        return False
    else:
        return True
      
      
def main():
    myDocument = {
        "Ticker" : "TP",
        "Profit Margin" : 0.128,
        "Institutional Ownership" : 0.146,
        "EPS growth past 5 years" : 0.149,
        "Total Debt/Equity" : 0.36,
        "Current Ratio" : 4,
        "Return on Assets" : 0.076,
        "Sector" : "Healthcare",
        "P/S" : 6.79,
        "Change from Open" : -0.0579,
        "Performance (YTD)" : 0.1308,
        "Performance (Week)" : 0.0011,
        "Quick Ratio" : 2.7,
        "Insider Transactions" : -0.1268,
        "P/B" : 3.51,
        "EPS growth quarter over quarter" : -0.15,
        "Payout Ratio" : 0.162,
        "Performance (Quarter)" : 0.0417,
        "Forward P/E" : 13.29,
        "P/E" : 14.5,
        "200-Day Simple Moving Average" : 0.1366,
        "Shares Outstanding" : 127,
        "Earnings Date" : datetime.datetime(2015,11,12,22,30),
        "52-Week High" : -0.0441,
        "P/Cash" : 5.44,
        "Change" : -0.0135,
        "Analyst Recom" : 1.4,
        "Volatility (Week)" : 0.0153,
        "Country" : "USA",
        "Return on Equity" : 0.171,
        "50-Day Low" : 0.0717,
        "Price" : 40.43,
        "50-Day High" : -0.0444,
        "Return on Investment" : 0.243,
        "Shares Float" : 130.22,
        "Dividend Yield" : 0.0055,
        "EPS growth next 5 years" : 0.0633,
        "Industry" : "Medical Laboratories & Research",
        "Beta" : 1.2,
        "Sales growth quarter over quarter" : -0.033,
        "Operating Margin" : 0.256,
        "EPS (ttm)" : 2.91,
        "PEG" : 1.26,
        "Float Short" : 0.019,
        "52-Week Low" : 0.6779,
        "Average True Range" : 0.53,
        "EPS growth next year" : 0.1271,
        "Sales growth past 5 years" : 0.011,
        "Company" : "SUPERCORP Inc.",
        "Gap" : 0,
        "Relative Volume" : 0.57,
        "Volatility (Month)" : 0.0277,
        "Market Cap" : 12455.2,
        "Volume" : 1777529,
        "Gross Margin" : 0.563,
        "Short Ratio" : 2.08,
        "Performance (Half Year)" : 0.1541,
        "Relative Strength Index (14)" : 56.22,
        "Insider Ownership" : 0.111,
        "20-Day Simple Moving Average" : -0.1722,
        "Performance (Month)" : 0.0044,
        "P/Free Cash Flow" : 14.43,
        "Institutional Transactions" : -0.1054,
        "Performance (Year)" : 0.3572,
        "LT Debt/Equity" : 0.88,
        "Average Volume" : 2147.14,
        "EPS growth this year" : 0.348,
        "50-Day Simple Moving Average" : -0.1125}
    print insert_document(myDocument)
    print "Document Created"

main()
