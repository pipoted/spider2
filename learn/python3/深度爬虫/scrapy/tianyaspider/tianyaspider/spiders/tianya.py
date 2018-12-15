# -*- coding: utf-8 -*-
import scrapy
import re

from tianyaspider.items import EmailSpiderItem


class TianyaSpider(scrapy.Spider):
    name = 'tianya'
    allowed_domains = ['tianya.com']
    start_urls = ['http://bbs.tianya.cn/m/post-140-393974-1.shtml']

    def parse(self, response):
        save_file = open('tianya.html', 'w')
        page_data = response.body.decode('utf-8', 'ignore')
        save_file.write(page_data)
        save_file.close()

        mail_regex = re.compile(r'([A-Z0-9.%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})', 
                                re.IGNORECASE)
        mail_list = mail_regex.findall(page_data)

        for mail in mail_list:
            my_item = EmailSpiderItem()
            my_item['email'] = mail
            my_item['url'] = 'http://bbs.tianya.cn/m/post-140-393974-1.shtml'

            yield my_item
