#!/usr/bin/env python
# coding=utf-8

from urllib import request

# 183.15.172.23:61430
# 183.15.172.23:61430
# '59.110.240.249:8080', '27.17.45.90:43411', '114.225.170.44:53128', '219.135.162.198:47201', '60.6.241.72:808', '61.135.217.7:80', '61.138.33.20:808', '59.52.185.54:808', '210.22.176.146:32153', '106.56.102.61:808', '171.38.25.79:8123', '121.33.220.158:808', '219.238.186.188:8118', '120.69.82.110:44693'

url = 'http://httpbin.org/ip'

# response = request.urlopen(url)
# print(response.read())

handler = request.ProxyHandler({
    'http': '59.110.240.249:8080',
})
opener = request.build_opener(handler)
response = opener.open(url)
print(response.read())

 
