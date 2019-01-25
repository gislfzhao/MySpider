# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
import random
import time
from urllib.parse import urlencode
import re
import os
import requests
from pyquery import PyQuery as pq
from multiprocessing.pool import Pool

# from User_Agents.UserAgents import USER_AGENTS
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
]


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
        'date': '2018-11-23',
        'page': 1,
        '_': str(int(time.time() * 1000))
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
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


def main_tencent_news():
    html = get_tencent_news_page()
    infos = parse_tencent_news_page(html)
    for info in infos:
        print(info)
        write_to_txt(info, "tencent_news")


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
        yield article


def write_to_txt(info, store_filename):
    with open(store_filename + '_result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(info, ensure_ascii=False) + "\n")


def get_article_info(articles):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': get_user_agent(),
        'Referer': 'http://news.qq.com/articleList/rolls/',
        'upgrade-insecure-requests': '1'
    }
    for article in articles:
        url = article.get('url')
        response = requests.get(url, headers=headers)
        if url and response.status_code == 200:
            doc = pq(response.text)
            catalog = doc('span.a_catalog').text()
            source = doc('span.a_source').text()
            contents = doc('#Cnt-Main-Article-QQ p.text').items()
            contents2 = list()
            for item in contents:
                # print(repr(item.text()))
                if item.text() in [' ', '', '\n']:
                    continue
                else:
                    contents2.append(item.text())
            content = '\n'.join(contents2)
            imgs = doc('#Cnt-Main-Article-QQ img').items()
            img_urls = list()
            for item in imgs:
                img_urls.append('https:' + item.attr('src'))
            article['catalog'] = catalog
            article['source'] = source
            article['content'] = content
            article['img_urls'] = img_urls
            article['store_path'] = re.sub(r'[\\/:*?"<>|\r\n]+', '-', article.get('title'))

        print(article)
        yield article


def save_images(article):
    if not os.path.exists('news1123/' + article.get('store_path')):
        if article.get('store_path'):
            os.mkdir('news1123/' + article.get('store_path'))
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': get_user_agent(),
            'upgrade-insecure-requests': '1'
        }
        if article.get('img_urls'):
            print(article.get('img_urls'))
            count = 0
            for url in article.get('img_urls'):
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    file_path = 'news1123/{0}/{1}.{2}'.format(article.get('store_path'), count, '.jpg')
                    if not os.path.exists(file_path):
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                    else:
                        print('Already Downloaded', file_path)
                count += 1
                break
    except requests.ConnectionError:
        print('Failed to Save Image')


if __name__ == '__main__':
    # main_tencent_news()
    news_jsons = get_tencent_roll_news()
    articles = parse_tencent_roll_news(news_jsons)
    articles2 = list(get_article_info(articles))
    if not os.path.exists('news1123'):
        os.mkdir('news1123')
    for article in articles2:
        write_to_txt(article, 'news1123/tencent_news')
    print(list(articles2))
    print(articles2)
    pool = Pool()
    pool.map(save_images, articles2)
    pool.close()
    pool.join()

