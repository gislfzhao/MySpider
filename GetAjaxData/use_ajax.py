# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import requests
import random
from pyquery import PyQuery as pq
from UseBasicLibrary.CrawlWebPage.UserAgents import USER_AGENTS


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_page():
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    headers = {
        'Host': 'm.weibo.cn',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'User-Agent': get_user_agent(),
        'X-Requested-With': 'XMLHttpRequest',
               }
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("ERROR:", e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            if item.get('card_type') == 9:
                item = item.get('mblog')
                weibo = dict()
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo
    pass


if __name__ == '__main__':
    json = get_page()
    for item in parse_page(json):
        print(item)
    pass
