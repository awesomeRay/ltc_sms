#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import time
from common.Config import config
import string

dbPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + "/db/tickers.json"

def initData():
    data = []
    dbFile = file(dbPath)
    content = dbFile.read()
    if content != '':
        data = json.loads(content, encoding="utf-8")
    dbFile.close()
    return data

# 启动时tickerList读入内存, 一开始没有数据是空list
tickers = initData();

def writeData():
    dbFile = open(dbPath, 'w')
    dbFile.write(json.dumps(tickers))
    dbFile.close()
    
    
def addTicker(ticker):
    if len(tickers) is config["tickerMaxLength"]:
        tickers.pop(0);
    tickers.append(ticker)
    return

def calcPoint(newestTicker):
    thePoint = None
    if len(tickers) > 0:
        minTicker = maxTicker = tickers[0]
        for ticker in tickers:
            if ticker["ticker"]["last"] > maxTicker["ticker"]["last"]:
                maxTicker = ticker
            elif ticker["ticker"]["last"] < maxTicker["ticker"]["last"]:
                minTicker = ticker
        upRange = (string.atof(newestTicker["ticker"]["last"]) - string.atof(minTicker["ticker"]["last"])) / string.atof(minTicker["ticker"]["last"])
        downRange = (string.atof(maxTicker["ticker"]["last"]) - string.atof(newestTicker["ticker"]["last"])) / string.atof(maxTicker["ticker"]["last"])
        if upRange > config["range"] :
            thePoint = generatePoint(upRange, 'up')
        elif downRange > config["range"] :
            thePoint = generatePoint(downRange, 'down')
    return thePoint

def generatePoint(theRange, trend):
    trendChar = ''
    if trend is 'up':
        trendChar = "起"
    else:
        trendChar = "下"
        
    point = {
             "message" : "【%s】了，幅度:%s,[%s]" % (trendChar, theRange, time.strftime('%Y-%m-%d %H:%M:%S')),
             "time" : time.time(),
             "trend" : trend
        }   
    return point
        