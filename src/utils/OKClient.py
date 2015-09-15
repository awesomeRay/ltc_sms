#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json


def getTicker():
    """
        获得最新的ltc价格
    """
    retSockFile = urllib.urlopen("https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny")
    ticker = json.loads(retSockFile.read())
    retSockFile.close()
    return ticker