#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  from scrapy import cmdline

#  cmdline.execute('scrapy crawl qqreaderspider'.split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from qqread.spiders.qqreaderspider import QqreaderspiderSpider

setting = get_project_settings()
process = CrawlerProcess(settings=setting)
process.crawl(QqreaderspiderSpider)
process.start()
