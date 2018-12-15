# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):
    def __init__(self):
        self.fp = open('1.txt', 'w')

    def process_item(self, item, spider):
        text = str(item) + '\r\n'
        self.fp.write(text)
        self.fp.flush()
        return item

    def __del__(self):
        pelf.fp.close()
