# -*- coding: utf-8 -*-
import requests
import json
import time
import csv
import re
import os
import lxml.html
from pyquery import PyQuery as pq
from urllib.parse import urlencode,quote,unquote
from SpiderPractise.CCTVnews.utils import get_user_agent,EARLY_SECTIONS


def get_sohu_news_list(page_num=1, page_size=25):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://mp.sohu.com/profile?xpt=c29odXptdGs4dXFkYkBzb2h1LmNvbQ==&_f=index_pagemp_1&spm=smpc'
                   '.content.author.1.15467611083904O9iT6C',
        'x-requested-with': 'XMLHttpRequest',
        'User-Agent': get_user_agent()
    }
    query_params = {
        'xpt': 'c29odXptdGs4dXFkYkBzb2h1LmNvbQ==',
        'pageNumber': page_num,
        'pageSize': page_size,
        'categoryId': '',
        '_': str(int(time.time() * 1000))
    }
    base_url = 'https://mp.sohu.com/apiV2/profile/newsListAjax?'
    try:
        url = base_url + urlencode(query_params)
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            print("Get Successfully!", url)
            return unquote(response.text)
        else:
            print("Get Failed", url)
            return None
    except Exception as e:
        print("ERROR", e.args)
        return None


def get_cctv_early_news(text):
    print("Get 早啊！新闻来了")
    if text:
        re_early = re.compile(r'早啊！新闻来了〔(.*?)〕\\",\\"url\\":\\"//(.*?)\\",\\"userid.*?', re.S)
        early_results = re.findall(re_early, text)
        for item in early_results:
            result = {
                "publish_time": item[0],
                "early_news_url": 'https://' + item[1]
            }
            print(result)
            yield result
    else:
        return None


def access_early_new_page(early_news):
    headers = {
        'Accept': 'text/html,application/xhtml+xmlw,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'Referer': 'https://mp.sohu.com/profile?xpt=c29odXptdGs4dXFkYkBzb2h1LmNvbQ==&_f=index_pagemp_1&spm=smpc'
        #            '.content.author.1.15467611083904O9iT6C',
        'upgrade-insecure-requests': '1',
        'User-Agent': get_user_agent()
    }
    for early_item in early_news:
        try:
            url = early_item.get('early_news_url')
            # url = 'https://www.sohu.com/a/286977075_115004'
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                print("Get Successfully!", url)
                articles = process_early_new_content(response.text)
                if len(articles) != 0:
                    print(articles)
                    save_early_new(early_item, articles)
            else:
                print("Get Failed", url)
        except Exception as e:
            print("Get Failed! ERROR:", e.args)


def process_early_new_content(text):
    print('Processing')
    doc = pq(text)
    article = doc('#mp-editor')
    child = article.children()[0]
    article_list = list()
    process_result = {
        'section': '',
        'content': '',
        'image': '',
        'video': '',
        'time': re.search('〔(.*?)〕', doc('#mp-editor > p:nth-child(1)').text(), re.S).group(1)
    }
    while child is not None:
        text = child.text_content().strip()
        if text == '今日提示':
            break
        elif text in EARLY_SECTIONS:
            process_result['section'] = text
        elif child.tag == 'ul':
            lis = child.findall('li')
            if len(lis) > 1:
                for i in range(len(lis) - 1):
                    if lis[i].text_content().strip() != '':
                        process_result['content'] = lis[i].text_content().strip()
                        print(process_result)
                        article_list.append(process_result.copy())
                        process_result['image'] = ''
                        process_result['content'] = ''
                        process_result['video'] = ''
            process_result['content'] = lis[len(lis) - 1].text_content().strip()
            while child.getnext().tag != 'ul' and child.getnext().text_content().strip() != '今日提示' \
                    and child.getnext().text_content().strip() not in EARLY_SECTIONS:
                child = child.getnext()
                if child.find('iframe') is None:
                    if child.find('img') is not None:
                        process_result['image'] = child.find('img').get('src')
                    else:
                        process_result['content'] += process_result.get('content') + child.text_content().strip()
                else:
                    process_result['video'] = child.find('iframe').get('src')
            print(process_result)
            article_list.append(process_result.copy())
            process_result['image'] = ''
            process_result['content'] = ''
            process_result['video'] = ''
        child = child.getnext()
    return article_list


def save_early_new(early_news, articles):
    filename = '早啊！新闻来了〔' + early_news.get('publish_time') + '〕.csv'
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:  # newline表示行与行之间
        fieldnames = ['section', 'content', 'image', 'video', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(articles)


def main():
    for i in range(10, 30):
        text = get_sohu_news_list(i)
        early_results = get_cctv_early_news(text)
        access_early_new_page(early_results)


if __name__ == '__main__':
    main()

