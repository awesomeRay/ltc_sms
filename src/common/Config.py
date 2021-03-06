#!/usr/bin/env python
# -*- coding: utf-8 -*-

import site
import json
import os

def initConfig():
    configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + "/conf/config.json"
    configFile = file(configPath)
    config = json.loads(configFile.read(), encoding="utf-8")
    configFile.close()
    return config

config = initConfig()
smsConfig = config["smsConfig"]

def getConfig():
    return config
