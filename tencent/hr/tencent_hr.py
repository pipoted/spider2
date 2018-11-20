#!/usr/bin/env python
# coding=utf-8

# 爬取腾讯招聘职位信息

import requests
from lxml import etree


URL = 'https://hr.tencent.com/position.php?keywords=python&tid=0&start=0#'


def get_url():
    """
    爬取所有的url
    """
    pass

def get_detail_urls():
    """
    获取每个url中的详细信息
    """
    pass

def spider():
    """
    循环爬取所有的url的详细信息
    """
    pass

if __name__ == '__main__':
    spider()
