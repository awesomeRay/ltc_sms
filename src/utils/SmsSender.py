#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import hashlib
import json

def md5(str):
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()

smsConfigFile = file("../../conf/config.json")
smsConfig = json.load(smsConfigFile)["smsConfig"]
smsConfigFile.close()

smsBaseUrl = smsConfig["url"] + "?%s"
smsParams = smsConfig["params"]
smsParams["pwd"] = md5(smsParams["sn"] + smsParams["pwd"]).upper()

smsParams["content"] = "testhello"

# print urllib.urlencode(params)
print smsBaseUrl % urllib.urlencode(smsParams)
response = urllib.urlopen(smsBaseUrl % urllib.urlencode(smsParams))
print response.read()


