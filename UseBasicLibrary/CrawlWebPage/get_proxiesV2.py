# -*- coding: utf-8 -*-
import json
import re
import time
import requests
import random
from UseBasicLibrary.CrawlWebPage.UserAgents import USER_AGENTS
from UseBasicLibrary.CrawlWebPage.PROXIES import PROXIES


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_proxies():
    return random.choice(PROXIES)


def get_one_page(url):
    while True:
        try:
            proxies = get_proxies()
            headers = dict()
            headers['User-Agent'] = get_user_agent()
            # print(proxies)
            # print(headers)
            res = requests.get(url, headers=headers, proxies=proxies, timeout=60)
            # res.encoding = "utf-8"
            if res.status_code == 200:
                return res.text
        except BaseException as e:
            print(e)
            time.sleep(30)


def parse_one_page(html):
    re_str = '<tr class=.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>.*?<a.*?>(.*?)</a>.*?<td.*?country.*?>(.*?)</td>' \
             '.*?<td>(.*?)</td>.*?<td.*?country.*?>.*?<td.*?country.*?>.*?title="(.*?)".*?<td>(.*?)</td>.*?<td>(.*?)' \
             '</td>.*?</tr>'
    pattern = re.compile(re_str, re.S)
    items = re.findall(pattern, html)
    if items is None:
        return {}
    else:
        for item in items:
            # yield 生成器, 会返回一个迭代器对象
            yield {
                'IP地址': item[0],
                '端口': item[1],
                '服务器地址': item[2],
                '是否匿名': item[3],
                '类型': item[4],
                '连接时间': item[5],
                '存活时间': item[6],
                '验证时间': item[7],
            }
    # print(items)


def write_to_file(content):
    # a 表示向文件追加，不会覆盖
    # filename = 'result' + time.strftime("_%Y_%m_%d_%H_%M_%S", time.gmtime()) + ".txt"
    with open('proxies_result4.txt', 'a', encoding="utf-8") as f:
        # print(type(json.dumps(content)))
        f.writelines(json.dumps(content, ensure_ascii=False) + "\n")
    f.close()


def main(offset=1):
    url = "http://www.xicidaili.com/nn/" + str(offset)
    html = get_one_page(url)
    # print(html)
    dict_iter = parse_one_page(html)
    for item in dict_iter:
        # print(item)
        write_to_file(item)
    # print(html)


if __name__ == "__main__":
    for i in range(100):
        main(random.randint(100, 201))
        print("已完成：" + str(i / 100 * 100) + "%")
        time.sleep(random.randint(60, 70))

