# coding=utf-8

import urllib.request
import urllib.parse


post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

city = input('城市：')

form_data = {
    'cname': city,
    'pid': '',
    'pageIndex': '1',
    'pageSize': '10',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

request = urllib.request.Request(url=post_url, headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())
