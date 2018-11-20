# coding=utf-8

import urllib.request
import urllib.parse
import os

url = 'https://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# 输入吧名，输入起始页码，输入结束页码，然后在当前文件中创建一个以吧名为名字的文件夹，里面是每一页的html内容，文件名是吧名_page.html

ba_name = input('吧名:')
start_page = int(input('起始页码：'))
end_page = int(input('结束页码:'))

if os.path.exists(ba_name):
    os.makedirs(name=ba_name)


for page in range(start_page, end_page + 1):
    # 拼接url的过程
    data = {
        'kw': ba_name,
        'pn': (page - 1) * 50,
    }
    data = urllib.parse.urlencode(data)
    url_temp = url + url
    request = urllib.request.Request(url=url_temp, headers=headers)
    print('从第%s页开始下载.....' % page)
    response = urllib.request.urlopen(request)

    filename = ba_name + '_' + str(page) + '.html'  # 拼接文件名
    filepath = ba_name + '/' + filename  # 拼接文件路径

    with open(filepath, 'wb') as fp:
        fp.write(response.read())
    print('从第%s页结束下载.....' % page)

print('下载结束')
