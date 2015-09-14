import urllib
import json

retSockFile = urllib.urlopen("https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny")
retObject = json.loads(retSockFile.read())
print retObject
print retObject["ticker"]