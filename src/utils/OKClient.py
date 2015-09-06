import urllib

f=urllib.urlopen("https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny")
s=f.read()
print s