# -*- coding: utf-8 -*-
import json
import random
import time
from urllib.parse import urlencode

import requests
from pyquery import PyQuery as pq

from User_Agents.UserAgents import USER_AGENTS


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_tencent_news_page(page=""):
    url = "https://news.qq.com/" + page
    headers = {
        'User-Agent': get_user_agent()
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(response.encoding)
        if response.status_code == 200:
            # print(response.text)
            return response.text
        else:
            time.sleep(10)
    except BaseException as e:
        print(e)


def parse_tencent_news_page(html):
    doc = pq(html)
    items = doc('div.Q-tpList').items()
    print(doc('div.Q-tpList'))
    for item in items:
        title = item('div.text a.linkto').text()
        link = item('div.text  a.linkto').attr('href')
        if title is None or link is None:
            continue
        yield {
            'title': title,
            'link': link
        }


def get_tencent_roll_news():
    url = "http://roll.news.qq.com/interface/cpcroll.php?"
    params = {
        'callback': 'rollback',
        'site': 'news',
        'mode': 1,
        'cata': '',
        'date': '2018-11-16',
        'page': 1,
        '_': str(int(time.time() * 1000))
    }
    headers = {
        'User-Agent': get_user_agent(),
        'Referer': 'http://news.qq.com/articleList/rolls/',
        'Host': 'roll.news.qq.com'
    }
    try:
        response = requests.get(url + urlencode(params), headers=headers, timeout=10)
        # print(response.encoding)
        # print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            return response.text
        else:
            time.sleep(10)
    except BaseException as e:
        print(e)


def parse_tencent_roll_news(jsons):
    rollback = eval(jsons[8:])
    article_info = rollback['data']['article_info']
    del rollback
    # 去除新闻链接的\
    article_info2 = list(map(lambda x: dict(zip(x, map(lambda value: value.replace('\\', ''), x.values()))),
                             article_info))
    del article_info
    for article in article_info2:
        print(article)


def main_tencent_news():
    html = get_tencent_news_page()
    infos = parse_tencent_news_page(html)
    for info in infos:
        print(info)
        write_to_txt(info, "tencent_news")


def write_to_txt(info, store_filename):
    with open(store_filename + '_result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(info, ensure_ascii=False) + "\n")


if __name__ == '__main__':
    # main_tencent_news()
    news_jsons = get_tencent_roll_news()
    parse_tencent_roll_news(news_jsons)
