# -*- coding: utf-8 -*-
import scrapy
from cyzonespider.items import ChuanyezhespiderItem
from lxml import etree


class ChuanyezheSpider(scrapy.Spider):
    name = 'chuanyezhe'
    allowed_domains = ['cyzone.cn']

    def start_requests(self):
        my_url = 'https://www.cyzone.cn/investor/list-0-1-0-0/'

        for i in range(1, 100):
            yield scrapy.Request(my_url % str(i), callback=self.parse)

    def parse(self, response):
        content = response.body
        my_tree = etree.HTML(content)

        trs = my_tree.xpath('//tr[@class="table-plate3"]')

        for tr in trs:
            my_item = ChuanyezhespiderItem()
            my_item['name'] = tr.xpath(
                './td[@class="people-name"]/a/text()')[0]
            my_item['company'] = tr.xpath('.//td[3]/a/text()')[0]
            my_item['work_name'] = tr.xpath('.//td[4]/text()')[0]
            my_item['about'] = tr.xpath('.//td[5]/a/text()')[0]

            yield my_item
