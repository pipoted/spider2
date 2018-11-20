#encoding:utf-8

import requests

# print(type(response.text))
# print(response.text)

# print(type(response.content))
# print(response.content.decode())

# print(response.url)
# print(response.encoding)
# print(response.status_code)

params = {
    'wd': '中国',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
url = 'https://www.baidu.com/'
response = requests.get(url=url, params=params,headers=headers)

with open('download/baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode())

print(response.url)

