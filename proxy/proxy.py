# -*- coding: utf8 -*-
"""Get Proxy Ip Module
"""


#encoding=utf8

import urllib2
from bs4 import BeautifulSoup
import requests


class ProxyIp(object):
    # get proxy-ip from this site
    # 国内高匿代理
    url = 'http://www.xicidaili.com/nn/{0}'

    @classmethod
    def update_ips(cls):
        """更新代理IP库
        """
        # 获取总页数
        # 要设置headers,不然会被认为是爬虫
        headers = {'user-agent': 'my-app/0.0.1'}
        resp = requests.get(cls.url.format(''), headers=headers).text
        soup = BeautifulSoup(resp, 'html.parser')
        divs = soup.findAll('div', {'class': 'previous'})
        if len(divs) == 0:
            return
        div = divs[0]
        pages_a = next_btn.previous_sibling
        print pages_a

    @classmethod
    def get_ips(cls):
        """返回所有的IP
        """
        pass

if __name__ == '__main__':
    ProxyIp.update_ips()
