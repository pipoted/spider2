#!/usr/bin/env python
# coding=utf-8

import time
import os
import re
import gevent
import queue

from queue import Queue
from gevent import monkey
from urllib import request

monkey.patch_all()

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

def get_host_name(httpstr):
    try:
        mail_regex = re.compile(r'(http://\S*?)/', re.IGNORECASE)
        my_list = mail_regex.findall(httpstr)

        if len(my_list) == 0:
            return None
        else:
            return my_list[0]
    except Exception as e:
        return None


def get_all_email(data):
    try:
        mail_regex = re.compile(r'([A-Z0-9.%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})',
                                re.IGNORECASE)
        my_list = mail_regex.findall(data)
        return my_list
    except Exception as e:
        return []


def get_all_http(data):
    try:
        mail_regex = re.compile(r'(http://\S*?)[\"|>|)]', re.IGNORECASE)
        my_list = mail_regex.findall(data)
        return my_list
    except Exception as e:
        return []


def get_data(url):
    try:
        data = request.urlopen(url).read().decode()
        return data
    except Exception as e:
        return ''


def BFS(url):
    global email_queue
    global url_queue


    page_data = get_data(url)
    print('抓取', url)
    email_list = get_all_email(page_data)
    if len(email_list) != 0:
        for email in email_list:
            print(email)
            email_queue.put(email)

    url_list = get_every_url(page_data)
    if len(url_list) != 0:
        for my_url in url_list:
            url_queue.put(my_url)


def save_mail():
    global email_queue
    mail_file = open('mail.txt', 'wb')
    while True:
        time.sleep(5)
        while not email_queue.empty():
            data = email_queue.get()
            mail_file.write((data + '\r\n').encode('utf8', 'ignore'))
            mail_file.flush()

        yield

    mail_file.close()


def BFSgo(url):
    global email_queue
    global url_queue

    url_queue.put(url)
    while True:
        time.sleep(5)
        url_list = []
        for i in range(100):
            if not url_queue.empty():
                url_list.append(url_queue.get())

        task_list = []
        for url in url_list:
            task_list.append(gevent.spawn(BFS, url))
        gevent.joinall(task_list)
        next(save_mail())
        print('save')


email_queue = Queue()
url_queue = Queue()

BFSgo('http://bbs.tianya.cn/m/post-140-393974-1.shtml')
