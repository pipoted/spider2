# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CyzonespiderPipeline(object):
    def __init__(self):
        self.fp = open('1.txt', 'w')

    def __del__(self):
        self.fp.close()

    def process_item(self, item, spider):
        if spider.name == 'chuanyezhe':
            print(item)
            self.fp.write(str(item), '\r\n')
            self.fp.flush()
            return item
