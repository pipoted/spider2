#!/usr/bin/env python
# coding=utf-8

import requests
from lxml import etree

BASE_DOMAIN = 'https://www.dytt8.net'
url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text

    html = etree.HTML(text)
    detail_urls = html.xpath('//table[@class="tbspan"]//a/@href')

    return map(lambda url: BASE_DOMAIN + url, detail_urls)


def parse_detail_page(url):
    movie = {}

    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)

    title = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    zoom = html.xpath('//div[@id="Zoom"]')[0]
    imgs = zoom.xpath('.//img/@src')

    cover = imgs[0]

    movie['title'] = title
    movie['cover'] = cover
    movie['screen_shot'] = 'screen_shot'

    infos = zoom.xpath('.//text()')
    for index, info in enumerate(infos):
        if info.startswith('◎产　　地'):
            info = info.replace('◎产　　地', '').strip()
            movie['country'] = info

        elif info.startswith('◎年　　代'):
            info = info.replace('◎年　　代', '').strip()
            movie['year'] = info

        elif info.startswith('◎译　　名'):
            info = info.replace('◎译　　名', '').strip()
            movie['translated'] = info

        elif info.startswith('◎片　　名'):
            info = info.replace('◎片　　名', '').strip()
            movie['name'] = info

        elif info.startswith('◎类　　别'):
            info = info.replace('◎类　　别', '').strip()
            movie['kind'] = info

        elif info.startswith('◎语　　言'):
            info = info.replace('◎语　　言', '').strip()
            movie['language'] = info

        elif info.startswith('◎字　　幕'):
            info = info.replace('◎字　　幕', '').strip()
            movie['subtitle'] = info

        elif info.startswith('◎上映日期'):
            info = info.replace('◎上映日期', '').strip()
            movie['show_date'] = info
            
        elif info.startswith('◎IMDb评分'):
            info = info.replace('◎IMDb评分', '').strip()
            movie['IMDB_grade'] = info
            
        elif info.startswith('◎豆瓣评分'):
            info = info.replace('◎豆瓣评分', '').strip()
            movie['douban_grade'] = info
            
        elif info.startswith('◎文件格式'):
            info = info.replace('◎文件格式', '').strip()
            movie['file_format'] = info
            
        elif info.startswith('◎视频尺寸'):
            info = info.replace('◎视频尺寸', '').strip()
            movie['video_size'] = info
            
        elif info.startswith('◎文件大小'):
            info = info.replace('◎文件大小', '').strip()
            movie['size'] = info
            
        elif info.startswith('◎导　　演'):
            info = info.replace('◎导　　演', '').strip()
            movie[' director'] = info
            
        elif info.startswith('◎编　　剧'):
            info = info.replace('◎编　　剧', '').strip()
            movie['scriptwriter'] = info
            
        elif info.startswith('◎主　　演'):
            info = info.replace('◎主　　演', '').strip()
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)

            movie['actors'] = actors
            
        elif info.startswith('◎标　　签'):
            info = info.replace('◎标　　签', '').strip()
            movie['tag'] = info
            
        elif info.startswith('◎简　　介'):
            info = info.replace('◎简　　介', '').strip()
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith('【下载地址】'):
                    movie['profile'] = profile

        elif info.startswith('◎获奖情况'):
            info = info.replace('◎获奖情况', '').strip()
            movie['praise'] = info

    download_url = html.xpath('//td[@bgcolor="#fdfddf"]/a/@href')
    movie['download_url'] = download_url

    return movie

    

def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []

    for x in range(1, 8):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)

        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)

    


if __name__ == '__main__':
    spider()
