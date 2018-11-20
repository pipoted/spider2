#!/usr/bin/env python
# coding=utf-8

import requests
import re


def parse_page(url):
    """TODO: Docstring for parse_page.

    :arg1: TODO
    :returns: TODO

    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    text = response.text

    titles = re.findall(r'<div\sclass="cont".*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class="source">.*<a.*?>(.*?)</a>', text)
    contents = re.findall(r'<div class="contson".*?>(.*?)</div>', text, re.DOTALL)
    peoms_temp = []
    for content in contents:
        content_temp = re.sub(r'<.*?>', ' ', content).strip()
        peoms_temp.append(content_temp)

    peoms = []
    for value in zip(titles, dynasties, authors, peoms_temp):
        title, dynasty, author, peom = value
        peom = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'peom': peom,
        }
        peoms.append(peom)

    return peoms


def main():
    """TODO: Docstring for main():.
    :returns: TODO

    """
    peoms = []
    for x in range(1, 100):
        url = 'https://www.gushiwen.org/default_{}.aspx'.format(x)
        peoms.append(parse_page(url))

    with open('gushi.text', 'w') as fp:
        fp.write(str(peoms))



if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
