from autodocparameters import recordparametertype
import autodocparameters
# -*- coding: utf-8 -*-
import scrapy
import re

from urllib import parse
from bs4 import BeautifulSoup
from baidubaike import items


class BaikeSpider(scrapy.Spider):
    name = 'bakei'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['http://baike.baidu.com/']

    def parse(self, response):
        pagedata = response.body
        url = response.url

    @recordparametertype
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
autodocparameters.logfunctionparameters()
