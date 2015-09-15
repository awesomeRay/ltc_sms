#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

dbPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + "/db/tickers.json"

def initData():
    data = None
    dbFile = file(dbPath)
    content = dbFile.read()
    if content != '':
        data = json.loads(content, encoding="utf-8")
    else:
        data = {}
    dbFile.close()
    return data

tickers = initData();

def writeData():
    dbFile = open(dbPath, 'w')
    print json.dumps(tickers)
    dbFile.write(json.dumps(tickers))
    dbFile.close()
