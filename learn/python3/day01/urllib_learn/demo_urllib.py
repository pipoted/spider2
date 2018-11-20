#!/usr/bin/env python
# coding=utf-8

from urllib import request
from urllib import parse

# urlopen
#response = request.urlopen('http://www.baidu.com')
## print(response.read())
##print(response.readlines())
#print(response.getcode())

# urlretrieve
# request.urlretrieve('http://www.baidu.com/', 'download/baidu.html')

# urlencoded
# parmes = {
#     'name':'张三',
#     'age':'18',
#     'greed':'hello',
# }
# result = parse.urlencode(parmes)
# print(result)
# url = 'http://www.baidu.com/s?'
# parme = {
#     'wd':'肖',
# }
# parme = parse.urlencode(parme)
# url += parme
# print(url)

# parse_qs 
url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%80%86%E6%B0%B4%E5%AF%92&oq=ip&rsv_pq=af8d8c0c00006d23&rsv_t=3361br50XDYR4Z77iG7A2aN4JV70WDS99OyE8T3puJ%2F4RyE4hlhVMCk9UCE&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=5&rsv_sug7=101&rsv_sug2=1&prefixsug=ni&rsp=3&inputT=3540&rsv_sug4=4801'
# print(parse.parse_qs(url))

# urlsplit urlparse 基本上完全相同， 但是 urlparse 中多了一个params属性
# result = parse.urlparse(url)
# print(result.scheme)
# print(result.netloc)
# result = parse.urlsplit(url)
# print(result)


