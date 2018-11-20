# coding=utf-8

import urllib.request
import urllib.parse
import urllib.error

url = 'http://www.google.com'

# response = urllib.request.urlopen(url)
# print(response)  # URLError

try:
    response = urllib.request.urlopen(url)
    print(response)
except urllib.error.URLError as e:
    print(e)
