# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time

from scrapy import signals
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(1)

        try:
            while True:
                show_more = self.driver.find_element_by_class_name('show-more')
                show_more.click()

                if not show_more:
                    break
        except:
            pass

        source = self.driver.page_source
        html = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return html
