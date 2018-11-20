#!/usr/bin/env python
# coding=utf-8

import requests
from lxml import etree

url = 'https://movie.douban.com/cinema/later/jian/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

response = requests.get(url, headers=headers)
text = response.text
movies = []

html = etree.HTML(text)
div = html.xpath('//*[@id="showing-soon"]')[0]

divs = div.xpath('//div[@class="item mod "]')
for div in divs:
    thumbnail = div.xpath('.//img/@src')
    title = div.xpath('.//a[@class=""]')[0].text
    show_date = div.xpath('.//ul/li[1]/text()')[0]
    kind = div.xpath('.//ul/li[2]/text()')[0]
    region = div.xpath('.//ul/li[3]/text()')[0]
    show_soon_movie = {
        'thumbnail':thumbnail,
        'title':title,
        'show_date':show_date,
        'kind':kind,
        'region':region,
    }
    movies.append(show_soon_movie)

divs_odd = div.xpath('//div[@class="item mod odd"]')
for div in divs:
    thumbnail = div.xpath('.//img/@src')
    title = div.xpath('.//a[@class=""]')[0].text
    show_date = div.xpath('.//ul/li[1]/text()')[0]
    kind = div.xpath('.//ul/li[2]/text()')[0]
    region = div.xpath('.//ul/li[3]/text()')[0]
    show_soon_movie = {
        'thumbnail':thumbnail,
        'title':title,
        'show_date':show_date,
        'kind':kind,
        'region':region,
    }
    movies.append(show_soon_movie)

print(movies)
