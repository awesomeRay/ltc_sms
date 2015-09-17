#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json
import time
import traceback

def getTicker():
    """
        获得最新的ltc价格
    """
    maxTryCount = 3
    success = False
    ticker = None
    while maxTryCount > 0 and not success:
        try:
            retSockFile = urllib.urlopen("https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny")
            ticker = json.loads(retSockFile.read())
            retSockFile.close()
            success = True
        except:
            print "call ok api error: " + traceback.format_exc()
            maxTryCount -= 1
            time.sleep(1)
            continue
    return ticker