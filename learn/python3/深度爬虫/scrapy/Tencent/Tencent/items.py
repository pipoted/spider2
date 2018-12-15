# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    detail_link = scrapy.Field()
    position_info = scrapy.Field()
    people_number = scrapy.Field()
    work_location = scrapy.Field()
    publish_time = scrapy.Field()
