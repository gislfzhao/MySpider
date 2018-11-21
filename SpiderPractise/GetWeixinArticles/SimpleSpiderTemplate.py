# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
from pickle import dumps
import re
from requests import Request

PROXY_POOL_URL = 'http://127.0.0.1:5000/random'


def get_proxy():
    """
    从代理池获取代理
    :return: 代理 or None
    """
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print("get proxy:", response.text)
            return response.text
    except ConnectionError:
        return None
    except Exception as e:
        print("ERROR", e.args)
        return None


def parse(response):
    # html = response.text
    # doc = pq(html)
    # items = doc('.news-box .news-list li .txt-box h3 a').items()
    # for item in items:
    #     url = item.attr('href')
    #     print(url)
    # nex = doc('#sogou_next').attr('href')
    # print(type(nex), str(nex))
    doc = pq(response.text)
    # testhtml = '    var publish_time = "2018-11-18" || "";'
    re_date = re.compile('.*?publish_time = "(\d+-\d+-\d+)" \|\| "".*?', re.S)
    data = {
        'title': doc('.rich_media_title').text().replace('\n', ''),
        'content': doc('.rich_media_content').text().replace('\n', '').replace('\t', ''),
        'date': re_date.search(response.text).group(1),
        'nickname': doc('#js_profile_qrcode .profile_nickname').text(),
        'wechat': doc('#js_profile_qrcode .profile_inner > p:nth-child(3) span').text(),
        'label': doc('#js_profile_qrcode .profile_inner > p:nth-child(4) span').text()
        #  nth-child(2)属于其父元素的第二个子元素
        #  p:nth-child(2)属于其父元素的第二个子元素的每个 p ,即找到所有p( p满足属于其父元素的第二个元素)
    }
    print(data)
    for key, value in data.items():
        print(key, value)


def main():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 "
                      "Safari/537.1 "
    }
    url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1542532720&ver=1252&signature=O6qKSy97KzTfp5yzUSxmbUOicerV' \
          '*akYjXy1Gfhuw*bFvpoNbY0OW5EHrh19dRrQGmBfnAZoWfWzB4lNXA*rhXlZorNHYDIniJftYw*VMQkBq36B08mOWIjdCFAB9p3S&new=1 '
    while True:
        proxies = {}
        proxy = get_proxy()
        if proxy:
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
        try:
            response = requests.get(url, headers=headers, proxies=proxies, verify=False)
            print(response.status_code)
            if response.status_code == 200:
                parse(response)
                break
        except requests.RequestException as e:
            print("ERROR", e.args)


class A(object):
    def __init__(self):
        self.name = "Zhao"


class WeixinRequest(Request):
    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=10):
        Request.__init__(self, method, url, headers)    # 调用父类的构造函数
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout


if __name__ == '__main__':
    # a = WeixinRequest(url="", callback=None)
    # print(a)
    # print(dumps(a))
    main()
