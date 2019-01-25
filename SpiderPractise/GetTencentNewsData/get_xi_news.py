# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests
import json
import time
import re
import csv
from pyquery import PyQuery as pq
from SpiderPractise.GetTencentNewsData.config import get_user_agent, LINK_HEADERS
from urllib.parse import urlencode
from multiprocessing import Pool


def get_page(base_url, params):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': get_user_agent(),
        'Host': 'cpc.people.com.cn',
        'Upgrade-Insecure-Requests': '1'
    }
    try:
        if params == dict():
            params = ''
        url = base_url + urlencode(params)
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            print("Get Successfully!", url)
            return response.text
        else:
            print("Get Failed", url)
            return None
    except Exception as e:
        print("ERROR", e.args)
        return None


def parse_page(text):
    doc = pq(text)
    start_url = 'http://cpc.people.com.cn'
    top = doc('.t2_top_img.clearfix')
    for item in top('a').items():
        yield start_url + item.attr('href')
    zhuanji = doc('.zhuanji_left.fl')
    for item in zhuanji('li').items():
        yield start_url + item('a').attr('href')


def get_parse_article_link(link_url):
    try:
        response = requests.get(link_url, headers=LINK_HEADERS, timeout=30)
        if response.status_code == 200:
            print("Get Successfully!", link_url)
            print(response.encoding)
            if response.encoding == 'ISO-8859-1':
                text = response.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8')
            else:
                text = response.text
            doc = pq(text)
            content = doc('.text_con.text_con01 .text_c')
            result = {
                'cover': content('.show_text img').attr('src'),
                'title': content('h1').text(),
                'web_url': link_url,
                'author': content('.sou a').text(),
                'time': re.search('(.*?)\s+.*?', content('.sou').text()).group(1)
            }
            if result['cover'] is None:
                result['cover'] = ''
            result['time'] = result['time'].replace('年', '-').replace('月', '-').replace('日', ' ')
            print(result)
            return result
        else:
            print("Get Failed", link_url)
            return None
    except Exception as e:
        print("ERROR", e.args)
        return None


def write_to_json(results):
    timename = time.strftime('%Y-%m-%d %H{}%M{}%S', time.localtime()).format("：", "：")
    filename = timename + '  xi_news.json'
    with open('news/'+filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(results, ensure_ascii=False))


def write_to_csv(results):
    timename = time.strftime('%Y-%m-%d %H{}%M{}%S', time.localtime()).format("：", "：")
    filename = timename + '  xi_news.csv'
    with open('news/' + filename, 'w', encoding='utf-8-sig', newline='') as f:      # newline表示行与行之间
        fieldnames = ['cover', 'title', 'web_url', 'author', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    result_list = list()
    base_url = "http://cpc.people.com.cn/xijinping/index.html"
    params = {}
    text = get_page(base_url, params)
    if text:
        results = parse_page(text)
        for result in results:
            if get_parse_article_link(result):
                result_list.append(get_parse_article_link(result))
        # pool = Pool()
        # pool.map(get_parse_article_link, results)
        # pool.close()
        # pool.join()
    # write_to_json(result_list)
    write_to_csv(result_list)


if __name__ == '__main__':
    main()



