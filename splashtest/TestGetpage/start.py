#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from TestGetpage.spiders.zj import ZjSpider

setting = get_project_settings()
process = CrawlerProcess(settings=setting)
process.crawl(ZjSpider)
process.start()
