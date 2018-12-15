# -*- coding: utf-8 -*-
import scrapy

from Tencent.items import TencentItem

class TencentHrSpider(scrapy.Spider):
    name = 'tencent_hr'
    offset = 0
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?keywords=python&start=0#a']

    def parse(self, response):
        for every_data in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            tencent_item = TencentItem()

            tencent_item['name'] = every_data.xpath('./td[1]/a/text()').extract()
            tencent_item['detail_link'] = every_data.xpath('./td[1]/a/@href').extract()
            tencent_item['position_info'] = every_data.xpath('./td[2]/text()').extract()
            tencent_item['people_number'] = every_data.xpath('./td[3]/text()').extract()
            tencent_item['work_location'] = every_data.xpath('./td[4]/text()').extract()
            tencent_item['publish_time'] = every_data.xpath('./td[5]/text()').extract()

            yield tencent_item

        if self.offset < 200:
            self.offset += 10

        new_url = 'https://hr.tencent.com/position.php?keywords=python&start='+str(self.offset)+'#a'
        yield scrapy.Request(new_url, self.parse)

        





        



