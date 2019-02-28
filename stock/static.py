#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#  url = 'http://quote.stockstar.com/stock/small_3_1_1.html'
#  url = 'http://www.zjzfcg.gov.cn/purchaseNotice/index.html?_=1546402255489'
url = 'http://www.zjzfcg.gov.cn/purchaseNotice/index.html?_=1546405964461'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

print(requests.get(url, headers=headers).content.decode('utf-8', 'ignore'))
