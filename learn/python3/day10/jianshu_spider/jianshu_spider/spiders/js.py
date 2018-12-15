# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="title"]/text()').get().strip()
        avatar = 'https:' + response.xpath('//a[@class="avatar"]/img/@src').get()
        author = response.xpath('//span[@class="name"]/a/text()').get().strip()
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get().replace('*', '')
        article_id = response.url.split('?')[0].split('/')[-1]
        content = response.xpath('//div[@class="show-content-free"]').get()
        word_count = response.xpath('//span[@class="wordage"]/text()').get().strip()
        read_count = response.xpath('//span[@class="views-count"]/text()').get().strip()
        like_count = response.xpath('//span[@class="likes-count"]/text()').get().strip()
        comment_count = response.xpath('//span[@class="comments-count"]/text()').get().strip()
        subjects = ','.join(response.xpath('//div[@class="include-collection"]/a/div/text()').getall())

        yield JianshuSpiderItem(
            title=title,
            avatar=avatar,
            author=author,
            pub_time=pub_time,
            origin_url=response.url,
            article_id=article_id,
            content=content,
            read_count=read_count,
            like_count=like_count,
            word_count=word_count,
            subjects=subjects,
            comment_count=comment_count,
        )
