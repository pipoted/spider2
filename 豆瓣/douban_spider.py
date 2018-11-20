# encoding=utf-8

import requests
from lxml import etree

# 爬取豆瓣电影正在上映的电影信息

# 将网站页面抓取下来
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
url = 'https://movie.douban.com/cinema/nowplaying/jian/'

response = requests.get(url, headers=headers)
text = response.text
movies = []


# 将抓取下来的数据按照一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath('//ul[@class="lists"]')[0]
lis = ul.xpath('.//li')

for li in lis:
    title = li.xpath('@data-title')
    score = li.xpath('@data-score')
    duration = li.xpath('@data-duration')
    region = li.xpath('@data-region')
    director = li.xpath('@data-director')
    actors = li.xpath('@data-actors')
    thumbnail = li.xpath('.//img/@src')

    movie = {
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail
    }
    movies.append(movie)

print(movies)


