#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

def initData():
    dbPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + "/db/tickers.json"
    dbFile = file(dbPath)
    tickers = json.loads(dbFile.read(), encoding="utf-8")
    dbFile.close()
    return tickers

tickers = initData();