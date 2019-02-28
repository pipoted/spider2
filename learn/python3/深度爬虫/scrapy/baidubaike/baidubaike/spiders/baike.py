# -*- coding: utf-8 -*-
import scrapy
import re

from baidubaike.items import BaidubaikeItem
from urllib import request
from bs4 import BeautifulSoup
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor


class BaikeSpider(CrawlSpider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']
    pagelinks = LinkExtractor(allow=('/item/.*'))
    rules = [Rule(pagelinks, callback='parse_item', follow=True)]

    def parse_item(self, response):
        pagedata = response.body
        baike_item = BaidubaikeItem()
        baike_item['name'] = str(self.get_title(pagedata))
        baike_item['content'] = str(self.get_content(pagedata))
        baike_item['url'] = response.url

        yield baike_item

    def get_title(self, pagedata):
        soup = BeautifulSoup(pagedata, 'html.parser')
        list1 = soup.find_all('h1')
        list2 = soup.find_all('h2')

        if len(list1) != 0 and len(list2) != 0:
            return (list1[0].text, list2[0].text)
        elif len(list1) != 0 and len(list2) == 0:
            return list1[0].text

    def get_content(self, pagedata):
        soup = BeautifulSoup(pagedata, 'html.parser')
        summary = soup.find_all('div', class_='lemma-summary')
        if len(summary) != 0:
            return summary[0].get_text()
        else:
            return None
