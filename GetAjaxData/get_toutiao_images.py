# -*- coding: utf-8 -*-
import requests
import os
import random
import time
from re import sub
from urllib.parse import urlencode
from UseBasicLibrary.CrawlWebPage.UserAgents import USER_AGENTS
from hashlib import md5
from multiprocessing.pool import Pool


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_page(offset=0):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街怕',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    headers = {
        'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'User-Agent': get_user_agent(),
        'X-Requested-With': 'XMLHttpRequest',
    }
    url = "https://www.toutiao.com/search_content/?" + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("ERROR:", e.args)
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            if not title:
                continue
            images = item.get('image_list')
            if not images:
                continue
            for image in images:
                yield {
                    'image_url': "http:" + image.get('url').replace('list', 'large') if isinstance(image, dict) else
                    "http:" + image.replace('list', 'large'),
                    'title': sub(r'[\\/:*?"<>|\r\n]+', '-', title)      # 删除不合法字符
                }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        headers = {
            'User-Agent': get_user_agent()
        }
        response = requests.get(item.get('image_url'), headers=headers)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), '.jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(0, 9)])
    pool.map(main, groups)
    pool.close()
    pool.join()
