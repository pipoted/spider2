# -*- coding: utf-8 -*-
import scrapy

from bmw.items import BmwItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
        ui_boxs = response.xpath('//div[@class="uibox"]')[1:]
        for ui_box in ui_boxs:
            category = ui_box.xpath('.//div[@class="uibox-title"]/a/text()').get()
            urls = ui_box.xpath('.//ul/li/a/img/@src').getall()
            urls = list(map(lambda url: response.urljoin(url), urls))

            yield BmwItem(category=category, image_urls=urls)
