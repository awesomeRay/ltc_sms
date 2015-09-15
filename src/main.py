#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils.SmsSender as smsSender
import utils.OKClient as OKClient
import TickerManager as tickerManager 
import json
from common.Config import config
import time

if __name__ == '__main__':
    while True:
        lastTicker = OKClient.getTicker()
        tickerManager.addTicker(lastTicker)
        point = tickerManager.calcPoint()
        if point is not None:
             lastPoint = getLastPoint()
             if point.time - lastPoint.time >=  config.maxWaitMilliSeconds or point.trend is not lastPoint.trend:
                 content = generateSmsContent(point)
                 smsSender.sendSms(content)
                 savePoint(point)
              
        time.sleep(config.interval)
    