# -*- coding: utf-8 -*-
import scrapy


class ZjSpider(scrapy.Spider):
    name = 'zj'
    allowed_domains = ['zjzfcg.gov.cn']
    start_urls = [
        'http://www.zjzfcg.gov.cn/purchaseNotice/index.html?_=1546405964461'
    ]

    def parse(self, response):
        print(response.body.decode('utf-8'))
        pass
