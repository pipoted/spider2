# -*- coding: utf-8 -*-
import scrapy
from qqread.items import QqreadItem
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

from lxml import etree


class QqreaderspiderSpider(CrawlSpider):
    name = 'qqreaderspider'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n10p1']
    rules = (Rule(
        LinkExtractor(allow=r'/bk/so2/n10p\d+'),
        callback='parse_booklist',
        follow=True), )

    def parse_booklist(self, response):
        content = response.body
        mytree = etree.HTML(content)

        book_info = mytree.xpath(
            '//div[@class="book"]/div[@class="book_info"]')
        for line in book_info:
            title = line.xpath('.//h3//text()')[-1]
            url = line.xpath('./h3/a/@href')[-1]
            print(title, url)

            yield scrapy.Request(url, callback=self.parse_book)

    def parse_book(self, response):
        my_item = QqreadItem()

        content = response.body
        mytree = etree.HTML(content)

        my_item['title'] = mytree.xpath(
            '//div[@class="title"]/strong/a/text()')[-1]
        #  print(title)
        my_item['tags'] = mytree.xpath(
            '//div[@class="tags"]/text()')[0].strip()
        #  print(tags)
        info = mytree.xpath('//div[@class="info"]//p/text()')

        line_str = ''
        for line in info:
            line_str += line

        my_item['content'] = line_str

        yield my_item
