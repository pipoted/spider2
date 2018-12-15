# -*- coding: utf-8 -*-
from _cffi_backend import callback

import scrapy
import re

from fang.items import NewHouseItem
from fang.items import ESFHouseItem


class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['http://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath('//table[@id="senfe"]//tr')
        province = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')
            province_td = tds[0]
            province_text = province_td.xpath('.//text()').get()
            province_text = re.sub(r'\s', '', province_text)
            if province_text:
                province = province_text
            if province == '其它':
                continue

            city_td = tds[1]
            city_links = city_td.xpath('.//a')
            for city_link in city_links:
                city_name = city_link.xpath('.//text()').get()
                city_url = city_link.xpath('.//@href').get()

                url_module = city_url.split('//')
                scheme = url_module[0]
                domain = url_module[1]

                if 'bj.' in domain:
                    newhouse_url = 'http://newhouse.fang.com/house/s/'
                    esf_url = 'http://esf.fang.com'
                else:
                    newhouse_url = scheme + '//' + 'newhouse.' + domain + '/house/s/'
                    esf_url = scheme + '//' + 'esf.' + domain

                # yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={'info': (province, city_name)})

                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={'info': (province, city_name)})

    def parse_newhouse(self, response):
        province, city_name = response.meta.get('info')
        lis = response.xpath('//div[@id="newhouse_loupai_list"]/ul/li')
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get().strip()
            try:
                price = li.xpath('.//div[@class="nhouse_price"]/span/text()').get() + li.xpath('.//div[@class="nhouse_price"]/em/text()').get()
            except:
                price = '价格待定'

            rooms = ''.join(li.xpath('.//div[@class="house_type clearfix"]//text()').getall())
            rooms = re.sub(r'\s', '', rooms)
            try:
                address = li.xpath('.//div[@class="address"]/a/text()').get().strip()
                address = re.sub(r'\s', '', address)
            except:
                address = None

            sale = li.xpath('/html/body/div[9]/div/div[1]/div[1]/div/div/ul/li[19]/div/div[2]/div[4]/span/text()').get()
            sale_house = li.xpath('/html/body/div[9]/div/div[1]/div[1]/div/div/ul/li[20]/div/div[2]/div[4]/a/text()').getall()
            if not sale_house:
                sale_house = None
            sale = {
                sale: sale_house,
            }
            try:
                origin_url = 'http:' + li.xpath('.//div[@class="nlcd_name"]/a/@href').get()
            except:
                origin_url = None

            yield NewHouseItem(
                province=province,
                city=city_name,
                name=name,
                price=price,
                rooms=rooms,
                address=address,
                sale=sale,
                origin_url=origin_url,
            )

        next_url = response.xpath('//a[@class="next"]/@href').get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, meta={'info': (province, city_name)})

    def parse_esf(self, response):
        province, city_name = response.meta.get('info')
        dls = response.xpath('//dl[@class="clearfix"]')
        item = ESFHouseItem(province=province, city=city_name)
        for dl in dls:
            name = dl.xpath('.//p[@class="add_shop"]/a/@title').get()
            infos = dl.xpath('.//p[@class="tel_shop"]/text()').getall()
            infos = list(map(lambda x: re.sub(r'\s', '', x), infos))

            for info in infos:
                if '厅' in info:
                    item['rooms'] = info
                elif '层' in info:
                    item['floor'] = info
                elif '向' in info:
                    item['toward'] = info
                elif '建' in info:
                    item['year'] = info.replace('建', '')
                elif '㎡' in info:
                    item['area'] = info

            address = dl.xpath('.//p[@class="add_shop"]/span/text()').get()
            item['address'] = address
            item['name'] = name

            # price = dl.xpath('.//dd[@class="price_right"]/span/text()').getall()
            price_behind = dl.xpath('.//dd[@class="price_right"]/span/text()').getall()[0]
            item['price'] = dl.xpath('.//dd[@class="price_right"]/span/b/text()').get() + price_behind
            item['unit'] = dl.xpath('.//dd[@class="price_right"]/span/text()').getall()[-1]

            item['origin_url'] = response.urljoin(dl.xpath('.//h4[@class="clearfix"]/a/@href').get())

            yield item

        next_url = response.xpath('//div[@id="list_D10_15"]//@href').get()

        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf, meta={'info': (province, city_name)})
