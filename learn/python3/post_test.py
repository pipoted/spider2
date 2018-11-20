# coding=utf-8

import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'

word = 'hello'

form_data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '814534.560887',
    'token': 'd3c106fbf26b2f362e4fefeb92d1ccfc',
}

headers = {
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '121',
    'Accept': '*/*',
    'Origin': 'https: // fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'charset': 'UTF-8',
    'Referer': 'https: // fanyi.baidu.com/translate?aldtype = 16047 & query = &keyfrom = baidu & smartresult = dict & lang = auto2zh',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN, zh q = 0.9, en q = 0.8',
    'Cookie': 'BAIDUID=6B3BA9FD32D10FF2AF8E75A7BEA1DE8F:FG=1; PSTM=1531444331; BIDUPSID=A742E017690AC402FECCCC02BA22FE10; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; PSINO=7; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BCLID=12843140544916603679; BDSFRCVID=sQ0sJeC62C0WJ8b7TKO3ei9ESmK2qw5TH6aIdqKWj3ry8voxGX1CEG0Pqx8g0Kub36t1ogKKQgOTHRjP; H_BDCLCKID_SF=tbkOoD_2JDvjD4-k247Hhn8thmT22-ust2kOQhcH0KLKMC_z5lLbjUFtDxcuJhvrbCviBUcMJxb1MRjvBPTo368SLpo8aRO7JDr2hq5TtUJ8SDnTDMRhqfTQ0tnyKMniLCv9-pn42ft0hC-CDj0-DjPW5ptX54rKMDOX343bHJO_bn66jbbkbftd2-teXq4tQnvAXJ3FbUb68I3KXfJBytKVhGjxJ5JZfJuD_KtMJDD5bIK9e-Rhq4tehHReQ6OeWDTm_DontU3kbb_63MRcDPLtetog2xPH-6kt-pPKKlTfqqv5M6bK2jkBhp7xXTom3mkjbPjyfn02OP5PDTjMDt4syPRIKMRnWNrBbIcJ-J8XhCtljT5P; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; H_PS_PSSID=1468_27209_21084_27401_26350_22073; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1541650531,1541740223,1541740243,1541757577; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1541757577',
}

request = urllib.request.Request(url=post_url, headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(url=post_url, data=form_data)
print(response.read())
