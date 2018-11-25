# -*- coding=utf-8 -*-

import requests
import time
import re

from lxml import etree


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python%20%E6%95%B0%E6%8D%AE?px=default&gx=%E5%85%A8%E8%81%8C&gj=&isSchoolJob=1&city=%E5%8C%97%E4%BA%AC',
    'Cookie': '_ga=GA1.2.619095963.1542095767; user_trace_token=20181113155607-939270b5-e719-11e8-889d-5254005c3644; LGUID=20181113155607-939273bf-e719-11e8-889d-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAAAGFABEF8D85F02E2B69372EBCF853F27AE50D72; _gat=1; LGSID=20181124135813-ee218233-efad-11e8-ba60-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20181124135841-fe5414c0-efad-11e8-ba60-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=1595135c88424fcf84702a3099282fc5',
}


def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&gx=全职&city=北京&needAddtionalResult=false&isSchoolJob=1'
    data = {
        'first': 'false',
        'pn': 1,
        'kd': 'python+数据',
    }

    # response = requests.post(url, headers=headers, data=data)
    # print(response.json()) # 将返回的json数据自动load成字典

    for x in range(1, 8):
        data['pn'] = x
        response = requests.post(url, headers=HEADERS, data=data)
        # print(response.json())
        result = response.json()
        positions = result['content']['positionResult']['result']

        for position in positions:
            position_id = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % position_id
            try:
                parse_position_detail(position_url)
            except IndexError:
                break

        time.sleep(2)


def parse_position_detail(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)

    position_name = html.xpath('//span[@class="name"]/text()')[0]
    job_request = html.xpath("//dd[@class='job_request']//span")

    salary = job_request[0].xpath('.//text()')[0].strip()
    city = job_request[1].xpath('.//text()')[0].strip()
    city = re.sub(r'[\s/]', '', city)
    work_years = job_request[2].xpath('.//text()')[0].strip()
    work_years = re.sub(r'[\s/]', '', work_years)
    education = job_request[3].xpath('.//text()')[0].strip()
    education = re.sub(r'[\s/]', '', education)

    desc = ''.join(html.xpath('//dd[@class="job_bt"]//text()')).strip()

    message = {
        'salary': salary,
        'city': city,
        'work_years': work_years,
        'education': education,
        'desc': desc,
    }

    with open('lagou_detail.txt', 'a') as fp:
        fp.write(str(message))
        print(salary)


def main():
    try:
        request_list_page()
    except Exception:
        pass


if __name__ == "__main__":
    main()
