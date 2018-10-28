# -*- coding: utf-8 -*-
import json
import re
import time
import requests
import random


def get_one_page(url):
    proxies = {
        "https": "https://171.37.152.66:8123"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers, proxies=proxies)
        # res.encoding = "utf-8"
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.exceptions as e:
        print(e)
        return None


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
    with open('proxies_result.txt', 'a', encoding="utf-8") as f:
        # print(type(json.dumps(content)))
        f.writelines(json.dumps(content, ensure_ascii=False) + "\n")
    f.close()


def main(offset=1):
    url = "http://www.xicidaili.com/nn/" + str(offset)
    html = get_one_page(url)
    dict_iter = parse_one_page(html)
    for item in dict_iter:
        # print(item)
        write_to_file(item)
    # print(html)


if __name__ == "__main__":
    for i in range(100):
        main()
        print("已完成：" + str(i / 100 * 100) + "%")
        time.sleep(random.randint(1, 3))

