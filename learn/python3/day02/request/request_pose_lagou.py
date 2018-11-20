#!/usr/bin/env python
# coding=utf-8

import requests

lagou_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python',
}
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

response = requests.post(url=lagou_url, data=data, headers=headers)
print(type(response.json()))
print(response.json().keys())

# with open('download/lagou.html', 'w', encoding='utf-8') as fp:

