#!/usr/bin/env python
# -*- coding: utf-8 -*-

import common.site
import utils.SmsSender as smsSender
import utils.OKClient as OKClient
import TickerManager as tickerManager 
import json
from common.Config import config
import time
import os


pointPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + "/db/lastPoint.json"

def getLastPoint():
    lastPoint = None
    lastPointFile = file(pointPath)
    content = lastPointFile.read()
    if content != '':
        lastPoint = json.loads(content, encoding="utf-8")
    lastPointFile.close()
    return lastPoint

def generateSmsContent(point):
    return config["smsConfig"]["prefix"] + point["message"] + config["smsConfig"]["suffix"]

def savePoint(point):
    pointFile = open(pointPath, 'w')
    pointFile.write(json.dumps(point))
    pointFile.close()

if __name__ == '__main__':
    while True:
        print time.time()
        newestTicker = OKClient.getTicker()
        point = tickerManager.calcPoint(newestTicker)
        if point is not None:
            lastPoint = getLastPoint()
            # maxWaitSeconds=1h 超过1h没有发过短信此次不论什么走势都发
            # 或者此次走势和上次走势不同， 就发
            if lastPoint is None or point["time"] - lastPoint["time"] >= config["maxWaitSeconds"] or point["trend"] is not lastPoint["trend"]:
                content = generateSmsContent(point)
                smsSender.sendSms(content)
                savePoint(point)
        tickerManager.addTicker(newestTicker)
        tickerManager.writeData()
        time.sleep(config["interval"])

