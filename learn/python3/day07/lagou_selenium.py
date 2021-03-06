# -*- coding=utf-8 -*-import reimport timefrom selenium import webdriverfrom lxml import etreeclass LagouSpider(object):    def __init__(self):        self.driver = webdriver.Chrome()        self.url = 'https://www.lagou.com/jobs/list_python?px=default&gx=&isSchoolJob=1&city=%E5%85%A8%E5%9B%BD#filterBox'        self.positions = []    def run(self):        self.driver.get(self.url)        while True:            source = self.driver.page_source            try:                self.parse_list_page(source)            except Exception as e:                pass            self.driver.switch_to.window(self.driver.window_handles[0])            next_btn = self.driver.find_element_by_xpath(                '//div[@class="pager_container"]/span[last()]')            next_btn.click()            time.sleep(2)        self.driver.quit()    def parse_list_page(self, source):        html = etree.HTML(source)        links = html.xpath('//a[@class="position_link"]/@href')        for link in links:            self.request_detail_page(link)            time.sleep(1)        self.driver.close()    def request_detail_page(self, url):        if len(self.driver.window_handles) == 1:            self.driver.execute_script('window.open("%s")' % url)        else:            self.driver.get(url)        self.driver.switch_to.window(self.driver.window_handles[-1])        source = self.driver.page_source        self.parse_detail_page(source)    def parse_detail_page(self, source):        html = etree.HTML(source)        position_name = html.xpath('//span[@class="name"]/text()')[0]        job_request = html.xpath("//dd[@class='job_request']//span")        salary = job_request[0].xpath('.//text()')[0].strip()        city = job_request[1].xpath('.//text()')[0].strip()        city = re.sub(r'[\s/]', '', city)        work_years = job_request[2].xpath('.//text()')[0].strip()        work_years = re.sub(r'[\s/]', '', work_years)        education = job_request[3].xpath('.//text()')[0].strip()        education = re.sub(r'[\s/]', '', education)        desc = ''.join(html.xpath('//dd[@class="job_bt"]//text()')).strip()        desc = re.sub(r'[\s/\\n\']', '', desc)        position = {            'position_name': position_name,            'salary': salary,            'city': city,            'work_years': work_years,            'education': education,            'desc': desc,        }        self.positions.append(position)        print(position)        print('-' * 50)if __name__ == "__main__":    spider = LagouSpider()    spider.run()