#!/usr/bin/env python
# coding=utf-8

from lxml import etree


parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tenxun.html', parser=parser)

# 1.获取所有的tr标签
# //tr
# trs = html.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode())

# 2.获取第二个tr标签
# trs = html.xpath('//tr[2]')[0]
# print(etree.tostring(trs, encoding='utf-8').decode())

# 3.获取所有class等于even的tr标签
# trs = html.xpath('//tr[@class="even"]')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode())

# 4.获取所有a标签中的href属性
a_list = html.xpath('//a/@href')
# for a in a_list:
#     print('http://hr.tencent.com/' + a)

# 5.获取所有的职位信息(纯文本)
trs = html.xpath('//tr[position() > 1]')
positions = []
for tr in trs:
    href = tr.xpath('.//a/@href')[0]
    fullurl = 'http://tr.tencent.com/' + href
    title = tr.xpath('./td[1]//text()')[0]
    category = tr.xpath('./td[2]/text()')
    nums = tr.xpath('./td[3]/text()')
    address = tr.xpath('./td[4]/text()')
    pub_time = tr.xpath('./td[5]/text()')
    
    position = {
        'url':fullurl,
        'title':title,
        'category':category,
        'nums':nums,
        'address':address,
        'pub_time':pub_time,
    }
    positions.append(position)

print(positions)
with open('download/tencent_hr.html', 'w') as fp:
    fp.write(str(positions))
