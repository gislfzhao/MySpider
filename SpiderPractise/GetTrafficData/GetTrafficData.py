# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random
import re
import requests
import json
import time

from UseBasicLibrary.CrawlWebPage.UserAgents import USER_AGENTS


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_page(page):
    headers = {
        'Origin': 'http: // www.nitrafficindex.com',
        'Referer': 'http://www.nitrafficindex.com/trafficIndexAnalysis.html',
        'User-Agent': get_user_agent(),
        'Host': 'www.nitrafficindex.com',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'areaCode': '110000',
        'roadLevel': '1, 2, 3, 4',
        'page': page,
        'rows': '1245',
    }
    url = 'http://www.nitrafficindex.com/traffic/getRoadIndex.do'
    try:
        response = requests.post(url, headers=headers, data=data)   # PSOT方法，表单数据进行爬取
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("ERROR:", e.args)
        return None


def parse_page(json):
    if json:
        try:
            # filename = re.sub(r'[\\/:*?"<>|\r\n]+', '-', json.get('date')) + ".txt"
            rows = json.get('rows')
            print(len(rows))
            for row in rows:
                yield {
                    'id': row.get('id'),
                    '名称': row.get('name'),
                    '起点': row.get('startName'),
                    '终点': row.get('endName'),
                    '交通指数': row.get('cIndex'),
                    '平均速度': row.get('avgspeed'),
                    '道路等级': row.get('roadGrade'),
                    '方向': row.get('dir'),
                    '时间': json.get('date')
                }
        except BaseException as e:
            print("ERROR", e.args)


def write_to_txt(item_road, filename):
    with open(filename, 'a', encoding="utf-8") as f:
        f.writelines(json.dumps(item_road, ensure_ascii=False) + "\n")


def main():
    json = get_page(1)
    items = parse_page(json)
    filename = time.strftime("%Y_%m_%d %H_%M", time.localtime()) + ".txt"
    for item in items:
        print(item)
        write_to_txt(item, filename)


if __name__ == '__main__':
    main()
