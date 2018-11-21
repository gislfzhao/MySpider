# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlencode
import random
import re
import os
import time
from multiprocessing import Pool
from bs4 import BeautifulSoup
from User_Agents.UserAgents import USER_AGENTS
from Proxy.Proxies import PROXYIES


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_user_proxy():
    return random.choice(PROXYIES)
    pass


def get_one_page(page_num):
    while True:
        params = {
            'p': page_num
        }
        headers = {
            'Referer': 'https://bing.ioliu.cn/',
            'User-Agent': get_user_agent()
        }
        proxies = get_user_proxy()
        url = "https://bing.ioliu.cn/?" + urlencode(params)
        try:
            response = requests.get(url, headers=headers, proxies=proxies)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return response.text
            else:
                time.sleep(10)
        except BaseException as e:
            print("ERROR", e.args)
            time.sleep(3)


def get_images_url(html):
    soup = BeautifulSoup(html, 'lxml')
    div_items = soup.find_all(name='div', attrs={'class': ['item']})
    for item in div_items:
        title = item.find(name='div', attrs={'class': ['description']}).find(name='h3').string.split(' (')[0]
        calendar = item.find(name='p', attrs={'class': ['calendar']}).find(name='em').string
        view = item.find(name='p', attrs={'class': ['view']}).find(name='em').string
        image_url = item.find(name='div', attrs={'class': ['card progressive']}).find(name='img')['src'].\
            replace('400x240', '1920x1080')
        yield {
            'title': re.sub(r'[\\/:*?"<>|\r\n]+', '-', title),
            'calendar': calendar,
            'view': view,
            'image_url': image_url
        }


def save_image(image_json):
    count = 0
    if not os.path.exists('bings_pictures'):
        os.mkdir('bings_pictures')
    while True:
        try:
            headers = {
                'Host': 'h1.ioliu.cn',
                'User-Agent': get_user_agent()
            }
            proxies = get_user_proxy()
            response = requests.get(image_json.get('image_url'), headers=headers)
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format('bings_pictures', image_json.get('title'), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        print("Downloading" + file_path)
                        f.write(response.content)
                    break
                else:
                    print('Already Downloaded', file_path)
                    break
            else:
                count += 1
                if count > 2:
                    print("break")
                    break
        except BaseException as e:
            print('Failed to Save Image', e.args)
            count += 1
            if count > 2:
                break


def main(num):
    html = get_one_page(num)
    jsons = get_images_url(html)
    if jsons:
        for item in jsons:
            print(item)
            save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x for x in range(1, 3)])
    pool.map(main, groups)
    pool.close()
    pool.join()
