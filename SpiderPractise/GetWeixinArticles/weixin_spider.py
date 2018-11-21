# -*- coding: utf-8 -*-
from requests import Session
from .redis_queue import RedisQueue
from .weixin_request import WeixinRequest
from .mysql_store import MySQL
from urllib.parse import urlencode
import requests
import re
from .setting import get_user_agent
from pyquery import PyQuery as pq
from requests import ReadTimeout, ConnectionError

PROXY_POOL_URL = 'http://127.0.0.1:5000/random'
MAX_FAILED_TIME = 30
DISABLE_PROXY_CODES = [1, 2, 3, 7, 8, 9, 12, 13, 17, 18, 20, 21, 26, 28]


class WeixinSpider:
    base_url = "https://weixin.sogou.com/weixin"
    keyword = 'NBA'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'IPLOC=CN1100; SUID=5B33F73C541C940A000000005ACDB92B; SUV=00CA47B13CF7335B5ACDB92B541EA651; '
                  'CXID=F847164F348BF105613A57B40BBE48E0; LSTMV=219%2C147; LCLKINT=1425; dt_ssuid=7991581200; '
                  'ssuid=4957928609; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; '
                  'sw_uuid=99467210; ABTEST=0|1542463013|v1; weixinIndexVisited=1; '
                  'SNUID=BA3A69EE595C2285F54D24B9590A2D14; sct=2; JSESSIONID=aaaqA7aAWxkn2aEIGMYBw',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': get_user_agent()
    }
    session = Session()
    redis_queue = RedisQueue()
    mysql = MySQL()

    def get_proxy(self):
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

    def start(self):
        """
        初始化工作
        :return:
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'type': '2', 'query': self.keyword})
        weixin_req = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.redis_queue.add(weixin_req)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_req = WeixinRequest(url, callback=self.parse_detail, need_proxy=True)
            yield weixin_req
        next_index = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next_index)
            weixin_req = WeixinRequest(url, callback=self.parse_index, need_proxy=True)
            yield weixin_req

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信工作号文章
        """
        doc = pq(response.text)
        re_date = re.compile('.*?publish_time = "(\d+-\d+-\d+)" \|\| "".*?', re.S)
        data = {
            'title': doc('.rich_media_title').text().replace('\n', ''),
            'content': doc('.rich_media_content').text().replace('\n', '').replace('\t', ''),
            'date': re_date.search(response.text).group(1),
            'nickname': doc('#js_profile_qrcode .profile_nickname').text(),
            'wechat': doc('#js_profile_qrcode .profile_inner > p:nth-child(3) span').text(),
            'label': doc('#js_profile_qrcode .profile_inner > p:nth-child(4) span').text()
        }
        yield data

    def start_request(self, weixin_res):
        """
        执行请求
        :param weixin_res: 请求
        :return: 响应
        """
        try:
            if weixin_res.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http': 'http://' + proxy,
                        'https': 'https://' + proxy
                    }
                    return self.session.send(weixin_res.prepare(), timeout=weixin_res.timeout,
                                             proxies=proxies, verify=False)
            return self.session.send(weixin_res.prepare(), timeout=weixin_res.timeout,
                                     verify=False)
        except (ConnectionError, ReadTimeout) as e:
            print("ERROR", e.args)
            return False

    def error(self, weixin_res):
        """
        错误处理
        :param weixin_res: 响应
        :return:
        """
        weixin_res.fail_time = weixin_res.fail_time + 1
        print('Request Failed', weixin_res.fail_time, 'Times', weixin_res.url)
        if weixin_res.fail_time < MAX_FAILED_TIME:
            if weixin_res.fail_time in DISABLE_PROXY_CODES:
                weixin_res.need_proxy = False
            else:
                weixin_res.need_proxy = True
            self.redis_queue.add(weixin_res)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.redis_queue.empty():
            weixin_res = self.redis_queue.pop()
            callback = weixin_res.callback
            print('Schedule', weixin_res.url)
            response = self.start_request(weixin_res)
            if response and response.status_code == 200:
                results = callback(response)
                if results:
                    for result in results:
                        print('New Result', result)
                        if isinstance(result, WeixinRequest):
                            self.redis_queue.add(result)
                        if isinstance(result, dict):
                            print(result)
                            self.mysql.insert('article', result)
                else:
                    self.error(weixin_res)
            else:
                self.error(weixin_res)

    def run(self):
        """
        运行
        :return:
        """
        self.start()
        self.schedule()
        self.mysql.close()
