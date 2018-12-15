# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()  # 小区名
    price = scrapy.Field()
    rooms = scrapy.Field()  # 居室数（列表）
    address = scrapy.Field()
    sale = scrapy.Field()  # 是否在售
    origin_url = scrapy.Field()  # 详情url


class ESFHouseItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    rooms = scrapy.Field()
    floor = scrapy.Field()
    toward = scrapy.Field()  # 朝向
    year = scrapy.Field()
    address = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()  # 总价
    unit = scrapy.Field()  # 单价
    origin_url = scrapy.Field()
