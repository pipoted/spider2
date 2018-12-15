# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random


class UserAgentDownloadMiddleware(object):
    USER_AGENT = [
        'Mozilla/5.0 (Macintosh U Intel Mac OS X 10_6_8 en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows U Windows NT 6.1 en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0 WOW64 rv:38.0) Gecko/20100101 Firefox/38.0',
        'Mozilla/5.0 (compatible MSIE 9.0 Windows NT 6.1 Trident/5.0',
        'Mozilla/4.0 (compatible MSIE 8.0 Windows NT 6.0 Trident/4.0)',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 6.0)',
        'Mozilla/4.0 (compatible MSIE 6.0 Windows NT 5.1)',
        'Mozilla/5.0 (Macintosh Intel Mac OS X 10.6 rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1 rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh Intel Mac OS X 10.6.8 U en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1 U en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 5.1 Maxthon 2.0)',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 5.1 TencentTraveler 4.0)',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 5.1)',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 5.1 The World)',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 5.1 360SE)',
        'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 5.1 Avant Browser)',
    ]

    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENT)
        request.headers['User-Agent'] = user_agent


class IPProxyDownloadMiddleware(object):
    PROXY_LIST = ['202.104.113.35:53281', '221.210.120.153:54402', '124.235.135.87:80', '222.171.251.43:40149',
                  '14.118.135.10:808', '183.3.150.210:41258', '121.33.220.158:808', '61.135.217.7:80',
                  '58.53.128.83:3128', '124.243.226.18:8888', '61.160.247.63:808', '117.114.149.66:53281',
                  '180.104.107.46:45700', '60.191.201.38:45461', '27.29.44.177:8118', '118.187.58.34:53281',
                  '221.224.136.211:35101', '116.192.175.93:41944', '106.12.7.54:8118', '171.38.27.127:8123',
                  '27.44.218.109:80', '61.135.155.82:443', '124.235.181.175:80', '106.15.42.179:33543',
                  '219.238.186.188:8118', '219.234.5.128:3128', '119.123.177.32:8888', '58.215.140.6:8080',
                  '58.52.170.225:808', '123.157.206.135:80', '139.199.38.182:8118']

    def process_request(self, request, spider):
        if 'proxy' not in request.meta:
            proxy_temp = self.get_proxy
            request.meta['proxy'] = proxy_temp

    def process_response(self, request, response, spider):
        if response.status != 200:
            return request

        return response


    @property
    def get_proxy(self):
        return 'https://' + random.choice(self.PROXY_LIST)
