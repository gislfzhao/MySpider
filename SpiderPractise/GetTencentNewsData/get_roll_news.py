# -*- coding: utf-8 -*-
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
        'User-Agent': get_user_agent(),
        'Referer': 'https://new.qq.com/rolls/?ext=news&day=20181207',
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
    content = eval(text[5:])
    results = list()
    for item in content.get('data'):
        result = {
            'cover': item.get('irs_imgs').get('294X195')[0],
            'title': item.get('title'),
            'web_url': item.get('url'),
            'author': item.get('source'),
            'time': item.get('publish_time')
        }
        print("Parse Successfully!", result)
        results.append(result)
    return results


def write_to_json(results):
    timename = time.strftime('%Y-%m-%d %H{}%M{}%S', time.localtime()).format("：", "：")
    filename = timename + '  roll_news.json'
    with open('news/'+filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(results, ensure_ascii=False))


def write_to_csv(results):
    timename = time.strftime('%Y-%m-%d %H{}%M{}%S', time.localtime()).format("：", "：")
    filename = timename + '  roll_news.csv'
    with open('news/' + filename, 'w', encoding='utf-8-sig', newline='') as f:      # newline表示行与行之间
        fieldnames = ['cover', 'title', 'web_url', 'author', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    base_url = "https://pacaio.match.qq.com/openapi/json?"
    params = {
        'key': 'news:' + time.strftime('%Y%m%d', time.localtime()),
        'num': 200,
        'page': 0,
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

