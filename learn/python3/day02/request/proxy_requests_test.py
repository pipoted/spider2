#!/usr/bin/env python
# coding=utf-8

import requests

# '61.135.217.7:80', '61.138.33.20:808', '60.6.241.72:808', '27.17.45.90:43411', '116.192.175.93:41944', '36.48.73.16:80', '123.206.86.26:80'

proxy = {
    'http':'61.138.33.20:808'
}

response = requests.get('http://httpbin.org/ip', proxies=proxy)
print(response.content.decode())
response = requests.get('http://httpbin.org/ip') 
print(response.content.decode())
