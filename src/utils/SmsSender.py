#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import hashlib

def md5(str):
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()

smsBaseUrl = "http://sdk2.entinfo.cn:8061/webservice.asmx/mdsmssend?%s"
sn = "SDK-SKY-010-01656"
pwd = md5(sn + "01656").upper()
mobile = "15972957263"

params = {
          "sn" : "SDK-SKY-010-194947",
          "pwd" : pwd,
          "mobile" : "15972957263",
          "content" : "2222",
          "ext" : "",
          "rrid" : "",
          "stime" : "",
          "msgfmt" : ""
          
    }
# print urllib.urlencode(params)
print smsBaseUrl % urllib.urlencode(params)
f = urllib.urlopen(smsBaseUrl % urllib.urlencode(params))
print f.read()


