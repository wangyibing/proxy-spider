# -*- coding: utf8 -*-
"""Get Proxy Ip Module
"""
#encoding=utf8

import urllib2
from lxml import etree
from pyvirtualdisplay import Display
from selenium import webdriver
import requests
import random
from time import sleep


class ProxyIp(object):
    # get proxy-ip from this site
    # 国内高匿代理
    url = 'http://www.xicidaili.com/nt/{0}'

    @classmethod
    def generate_headers(cls):
        """随机生成 request-headers
        """
        head_connection = ['Keep-Alive','close']
        head_accept = ['text/html, application/xhtml+xml, */*']
        head_accept_language = ['zh-CN,fr-FR;q=0.5',
            'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
        head_user_agent = [
            'Mozilla/5.0 (Windows NT 6.3; WOW64; \
                    Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; \
                    .NET CLR 2.0.50727; .NET CLR 3.5.30729; \
                    .NET CLR 3.0.30729; Media Center PC 6.0;\
                    .NET4.0C; rv:11.0) like Gecko)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2) \
                    Gecko/2008070208 Firefox/3.0.1',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1) \
                    Gecko/20070309 Firefox/2.0.0.3',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1) \
                    Gecko/20070803 Firefox/1.5.0.12',
            'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
            'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
            'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) \
                    Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
            'Mozilla/4.0 (compatible; MSIE 8.0; \
                    Windows NT 6.1; Win64; x64; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; \
                    Trident/6.0; SLCC2; .NET CLR 2.0.50727; \
                    .NET CLR 3.5.30729; .NET CLR 3.0.30729; i\
                    Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 i\
                    (KHTML, like Gecko) Maxthon/4.0.6.2000 \
                    Chrome/26.0.1410.43 Safari/537.1 ',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; \
                    Trident/6.0; SLCC2; .NET CLR 2.0.50727; \
                    .NET CLR 3.5.30729; .NET CLR 3.0.30729; \
                    Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E;\
                    QQBrowser/7.3.9825.400)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) \
                    Gecko/20100101 Firefox/21.0 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 \
                    (KHTML, like Gecko) Chrome/21.0.1180.92 \
                    Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; \
                    Trident/6.0; BIDUBrowser 2.x)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 \
                    (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 \
                    Safari/536.11']
        headers = {
            'Connection': head_connection[0],
            'Accept': head_accept[0],
            'Accept-Language': head_accept_language[1],
            'User-Agent': head_user_agent[random.randrange(
                0, len(head_user_agent))]
        }
        return headers

    @classmethod
    def update_ips(cls):
        """更新代理IP库
        """
        # display = Display(visible=0, size=(1024, 768))
        # display.start()
        browser = webdriver.Chrome('/home/bing/chromedriver')
        total = cls.get_total_pages(browser)
        with open('ips.txt', 'w') as f:
            for i in range(total):
                print i+1
                link = cls.url.format(i+1)
                browser.get(link)
                rows = browser.find_elements_by_xpath('//*[@id="ip_list"]/tbody/tr')
                rows = rows[1:]
                for row in rows:
                    txt = row.text.replace('\n', '').encode('utf-8')
                    f.write(txt+'\n')
                sleep(1)

        browser.close()
        # display.stop()

    @classmethod
    def get_total_pages(cls, browser):
        if not browser:
            return 0
        target = cls.url.format(1)
        browser.get(target)
        e = browser.find_element_by_xpath('//*[@id="body"]/div[2]/a[10]')
        return int(e.text)



    @classmethod
    def get_ips(cls):
        """返回所有的IP
        """
        pass

if __name__ == '__main__':
    ProxyIp.update_ips()
