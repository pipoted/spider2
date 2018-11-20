#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar


ALL_DATA = []


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    text = response.content.decode()
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')

    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')

            city_td = tds[0]
            if index == 0:
                city_td = tds[1]

            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            local_data = {
                'city':city,
                'min_temp': int(min_temp),
            }
            ALL_DATA.append(local_data)


def main():
    # url = 'http://www.weather.com.cn/textFC/hb.shtml'
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]

    for url in urls:
        parse_page(url)


    # 分析数据
    # 根据最低气温进行排序
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    data = ALL_DATA[:10]

    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda x: x['min_temp'], data))

    chart = Bar('中国最低气温排行榜')
    chart.add('', cities, temps)
    chart.render(path='temperature.html')


if __name__ == "__main__":
    main()
