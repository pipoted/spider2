#!/usr/bin/env python
# coding=utf-8

from urllib import request


url = 'http://www.renren.com/968661159'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Cookie': 'anonymid=joe6opt4-d0oy2b; depovince=ZGQT; _r01_=1; ick_login=4da537d3-0449-4966-b66f-496a222dae57; JSESSIONID=abcBbfvEYVqii9UprIhCw; jebe_key=19dce613-461f-4587-ab81-8d22a3eec391%7C845de2d6c5023d90e8d12e30054d2a36%7C1542019687288%7C1%7C1542019687294; t=78b85d7525616059f72128e1cc60b4979; societyguester=78b85d7525616059f72128e1cc60b4979; id=968661159; xnsid=f8766c9f; ch_id=10050; BAIDU_SSP_lcr=https://www.baidu.com/link?url=rKZCNyD_eTfg-8RnEY237jD9wzGBDH2JmS8rPvGj42i&wd=&eqid=c1a87ace000a230c000000065be97205; wp_fold=0; jebecookies=d14f72bd-3c04-487e-9140-4ab26965991f|||||; ver=7.0; loginfrom=null',
}

req = request.Request(url, headers=headers)
response = request.urlopen(req)

with open('download/renren.html', 'w', encoding='utf-8') as fp:
    fp.write(response.read().decode())
