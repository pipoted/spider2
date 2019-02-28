import requests
from lxml import etree

#  url = 'https://www.cyzone.cn/founder/list-0-1/'
url = 'https://www.cyzone.cn/event/list-0-1-0-0-0-0/0'

#  print(requests.get(url).text)
content = requests.get(url).text
my_tree = etree.HTML(content)

trs = my_tree.xpath('//tr[@class="table-plate3"]')

#  for tr in trs:
#  name = tr.xpath('./td[@class="people-name"]/a/text()')
#  company = tr.xpath('.//td[3]/a/text()')
#  positon = tr.xpath('.//td[4]/text()')
#  field = tr.xpath('.//td[5]/a/text()')
#  print(field)

for tr in trs:
    name = tr.xpath('./td[@class="tp2"]//span[1]/a/text()')
    company = tr.xpath('./td[@class="tp2"]//span[2]/text()')
    money = tr.xpath('.//div[@class="money"]/text()')
    round = tr.xpath('.//td[4]/text()')
    investor = tr.xpath('./td[@class="tp3"]/a/text()')
    industry = tr.xpath('./td[6]/a/text()')
    time = tr.xpath('./td[7]/text()')

    if company == []:
        company = name

    print(name, company, money, round, investor, industry, time)
