# -*- coding: utf-8 -*-
import requests
import json
import time
import csv
from SpiderPractise.GetTencentNewsData.config import get_user_agent
from urllib.parse import urlencode


def get_page(base_url, params):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': get_user_agent(),
        'Referer': 'https://new.qq.com/hot/?ext=world',
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
    content = json.loads(text[6:len(text)-1])
    results = list()
    for item in content.get('data'):
        result = {
            'cover': item.get('img'),
            'title': item.get('title'),
            'web_url': item.get('vurl'),
            'author': item.get('source'),
            'time': item.get('update_time')
        }
        print("Parse Successfully!", result)
        results.append(result)
    return results


def write_to_json(results):
    timename = time.strftime('%Y-%m-%d %H{}%M{}%S', time.localtime()).format("：", "：")
    filename = timename + '  hot_worlds_news.json'
    with open('news/'+filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(results, ensure_ascii=False))


def write_to_csv(results):
    timename = time.strftime('%Y-%m-%d  %H{}%M{}%S', time.localtime()).format("：", "：")
    filename = timename + '  hot_worlds_news.csv'
    with open('news/' + filename, 'w', encoding='utf-8-sig', newline='') as f:      # newline表示行与行之间
        fieldnames = ['cover', 'title', 'web_url', 'author', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    base_url = "https://pacaio.match.qq.com/irs/rcd?"
    params = {
        'cid': 137,
        'token': 'd0f13d594edfc180f5bf6b845456f3ea',
        'id': '',
        'ext': 'world',
        'num': 60,
        'expIds': '',
        'callback': '__jp0',
    }
    text = get_page(base_url, params)
    if text:
        results = parse_page(text)
        # write_to_json(results)
        write_to_csv(results)


if __name__ == '__main__':
    main()
