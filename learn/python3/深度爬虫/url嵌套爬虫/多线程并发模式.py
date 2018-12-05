# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-05 11:26'

import re
from queue import Queue
from urllib import request


def get_data(url):
    try:
        data = request.urlopen(url).read().decode()
        return data
    except:
        return ''


def get_email(data):
    try:
        mail_regex = re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', re.IGNORECASE)
        my_list = mail_regex.findall(data)
        return my_list
    except:
        return []


def get_host_name(httpstr):
    try:
        mail_regex = re.compile(r'(http://\S*?)/', re.IGNORECASE)
        my_list = mail_regex.findall(httpstr)
        if len(my_list) == 0:
            return None
        else:
            return my_list[0]
    except:
        return None


def get_every_url(data):
    all_list = []
    my_list1 = []
    my_list2 = []

    my_list1 = get_all_http(data)
    if len(my_list1) > 0:
        my_list2 = get_abs_url(my_list1[0], data)

    all_list.extend(my_list1)
    all_list.extend(my_list2)
    return all_list


def get_abs_url(url, data):
    try:
        regex = re.compile('href="(.*?)"', re.IGNORECASE)
        http_list = regex.findall(data)
        new_http_list = http_list.copy()
        for data in new_http_list:
            if data.find('http://') != -1:
                http_list.remove(data)
            if data.find('javascript') != -1:
                http_list.remove(data)
        host_name = get_host_name(url)
        if host_name != None:
            for i in range(len(http_list)):
                http_list[i] = host_name + http_list[i]
        return http_list
    except:
        return []


def get_all_http(data):
    try:
        mail_regex = re.compile(r'(http://\S*?)[\"|>|)]', re.IGNORECASE)
        my_list = mail_regex.findall(data)
        return my_list
    except:
        return []


def BFS(url):
    """
    广度遍历url
    """
    queue = Queue()
    queue.put(url)
    while not queue.empty():
        url = queue.get()
        print('抓取', url)
        page_data = get_data(url)
        email_list = get_email(page_data)
        if len(email_list) != 0:
            for email in email_list:
                print(email)

        url_list = get_every_url(page_data)  # 提取url压入到队列中
        if len(url_list) != 0:
            for url in url_list:
                queue.put(url)
                print(url)


BFS('http://bbs.tianya.cn/m/post-140-393974-4.shtml')

# print(get_email(get_data('http://bbs.tianya.cn/m/post-140-393974-1.shtml')))
# print(get_every_url(get_data('http://bbs.tianya.cn/m/post-140-393974-1.shtml')))
