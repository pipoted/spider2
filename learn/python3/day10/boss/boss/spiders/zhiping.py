# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipingSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),  # 列表页
        Rule(LinkExtractor(allow=r'.+/job_detail/\w+\~.html'), callback='parse_job', follow=False),  # 详情页
    )

    def parse_job(self, response):
        title = response.xpath('//div[@class="name"]/h1/text()').get().strip()
        salary = response.xpath('//span[@class="badge"]/text()').get().strip()
        info_primarys = response.xpath('//div[@class="info-primary"]/p//text()').getall()
        city = info_primarys[0].split('：')[-1].strip()
        experience = info_primarys[1].split('：')[-1].strip()
        education = info_primarys[2].split('：')[-1].strip()
        company = response.xpath('//a[@ka="job-detail-company"]/@title').get().strip()

        yield BossItem(title=title, salary=salary, city=city, experience=experience, education=education,
                       company=company)
