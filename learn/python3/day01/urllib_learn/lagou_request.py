#!/usr/bin/env python
# coding=utf-8

from urllib import request
from urllib import parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
post_url = 'https://www.lagou.com/jobs/companyAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
}
form_data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python',
}
form_data = parse.urlencode(form_data).encode()

req = request.Request(post_url, headers=headers, data=form_data, method='post')
response = request.urlopen(req)
print(response.read())
