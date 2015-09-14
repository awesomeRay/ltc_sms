#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import hashlib
import json
import common.site
import common.Config

def md5(contentStr):
    m = hashlib.md5()   
    m.update(contentStr)
    return m.hexdigest()

smsConfig = common.Config.smsConfig

smsBaseUrl = smsConfig["url"] + "?%s"
smsParams = smsConfig["params"]
smsParams["pwd"] = md5(smsParams["sn"] + smsParams["pwd"]).upper()


# content必须以中文开头，且长度不小于10个字符
def sendSms(content):
    smsParams["content"] = content
    # print urllib.urlencode(params)
    print smsBaseUrl % urllib.urlencode(smsParams)
    response = urllib.urlopen(smsBaseUrl % urllib.urlencode(smsParams))
    print response.read()

print 123

if __name__ == "__main__":
    sendSms("请注意，")


