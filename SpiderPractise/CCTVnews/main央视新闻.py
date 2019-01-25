# -*- coding: utf-8 -*-
import csv
import datetime
import re
import time
from urllib.parse import urlencode

import requests
from pyquery import PyQuery as pq

from SpiderPractise.CCTVnews.utils import get_user_agent, EARLY_SECTIONS


def sogou_weixin_page(t='2019.01.08'):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'wx.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': get_user_agent()
    }
    query_params = {
        'type': 2,
        's_from': 'input',
        'query': '早啊！新闻来了〔%s〕' % t,
        'ie': '',
        '_sug_': 'n',
        '_sug_type_': ''
    }
    base_url = 'https://wx.sogou.com/weixin?'
    try:
        url = base_url + urlencode(query_params)
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            print("Get Successfully!", url)
            if response.encoding == 'ISO-8859-1':
                text = response.text.encode('ISO-8859-1').decode('utf-8')
            else:
                text = response.text
            if text:
                doc = pq(text)
                news_li = doc('.news-list > li').items()
                for li in news_li:
                    if '央视新闻' in li('.txt-box .s-p').text():
                        early_news = {
                            'title': '早啊！新闻来了〔%s〕' % t,
                            'url': li('.img-box a').attr('href')
                        }
                        return early_news
                return None
        else:
            print("Get Failed", url)
            return None
    except Exception as e:
        print("ERROR", e.args)
        return None


def cctv_early_news_page(early_news):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'mp.weixin.qq.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': get_user_agent()
    }
    if early_news:
        try:
            url = early_news.get('url')
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                print("Get Successfully!", url)
                early_results = process_early_new_content(response.text)
                print(early_results)
                save_early_new(early_news, early_results)
            else:
                print("Get Failed", url)
        except Exception as e:
            print("Get Failed! ERROR:", e.args)


def process_early_new_content(text):
    print('Processing')
    doc = pq(text)
    article = doc('#js_content')
    child = article.children()[0]
    print(article.children())
    article_list = list()
    process_result = {
        'layer': 'flashNewsLayer',
        'content1': '',
        'flashnews_image': 'no',
        'discard': 'no',
        'region': '',
        'latitude': '',
        'longitude': '',
        'detail_url': '',
        'flashnews_video': '',
        'section': '',
        'time': re.search('〔(.*?)〕', doc('#activity-name').text().strip(), re.S).group(1)
    }
    while child is not None:
        if child.tag == 'section':
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
                        if lis[i].find('.//a') is not None:
                            process_result['detail_url'] = child.find('.//a').get('href')

                        process_result['content1'] = ''.join(lis[i].xpath('./p/text()')).strip()
                        if process_result['content1'] == '':
                            process_result['content1'] = ''.join(lis[i].xpath('./p/span/text()')).strip()
                            if process_result == '':
                                process_result['content1'] = lis[i].text_content().strip()
                        child2 = lis[i].findall('p')
                        for p in range(len(child2)):
                            if child2[p].find('img') is not None:
                                process_result['flashnews_image'] = child2[p].find('img').get('data-src')
                        print(process_result)
                        article_list.append(process_result.copy())
                        process_result['detail_url'] = ''
                        process_result['flashnews_image'] = 'no'
                        process_result['content1'] = ''
                        process_result['flashnews_video'] = ''

            if lis[len(lis) - 1].find('.//a') is not None:
                process_result['detail_url'] = lis[len(lis) - 1].find('.//a').get('href')
            process_result['content1'] = ''.join(lis[len(lis) - 1].xpath('./p/text()')).strip()
            if process_result['content1'] == '':
                process_result['content1'] = ''.join(lis[len(lis) - 1].xpath('./p/span/text()')).strip()
                if process_result['content1'] == '':
                    process_result['content1'] = lis[len(lis) - 1].text_content().strip()
            while child.getnext().tag != 'ul' and child.getnext().tag != 'section' and \
                    child.getnext().text_content().strip() != '今日提示' \
                    and child.getnext().text_content().strip() not in EARLY_SECTIONS:
                child = child.getnext()
                if child.find('iframe') is None:
                    if child.find('img') is not None:
                        process_result['flashnews_image'] = child.find('img').get('data-src')
                else:
                    process_result['flashnews_video'] = child.find('iframe').get('data-src')
            print(process_result)
            article_list.append(process_result.copy())
            process_result['detail_url'] = ''
            process_result['flashnews_image'] = 'no'
            process_result['content1'] = ''
            process_result['flashnews_video'] = ''
        child = child.getnext()
    return article_list


def save_early_new(early_news, articles):
    filename = early_news.get('title') + '.csv'
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:  # newline表示行与行之间
        fieldnames = ['layer', 'content1', 'flashnews_image', 'discard', 'region', 'latitude', 'longitude',
                      'detail_url', 'flashnews_video', 'section', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(articles)


def main():
    begin = datetime.date.today()
    end = datetime.date.today()
    d = begin
    delta = datetime.timedelta(days=1)
    while d <= end:
        print(d.strftime('%Y.%m.%d'))
        early_news = sogou_weixin_page(d.strftime('%Y.%m.%d'))
        print(early_news)
        # early_news['url'] = 'https://mp.weixin.qq.com/s?src=11&timestamp=1547939322&ver=1317&signature=4M5QjaaHmbd0DST11jypZEmWJxh64TOXiKoaG3hZV8MmkTbX7gxwahLPviJ6cQSxeFbbW0*p1Ops6y7Cs029QLbsjJ*cqCAnIp72J4wfM6V8APXSS7AfL1OrWjgao3eg&new=1'
        cctv_early_news_page(early_news)
        d += delta
        time.sleep(10)

    # early_results = get_cctv_early_news(text)
    # access_early_new_page(early_results)


if __name__ == '__main__':
    main()
