# -*- coding: utf-8 -*-
import json
import random
import re
import time
from bs4 import BeautifulSoup
import requests
import xlwings as xw
from lxml import etree

from UseBasicLibrary.CrawlWebPage.PROXIES import PROXIES
from UseBasicLibrary.CrawlWebPage.UserAgents import USER_AGENTS


def get_user_agent():
    return random.choice(USER_AGENTS)


def get_proxies():
    return random.choice(PROXIES)


def get_one_page(url):
    while True:
        try:
            # proxies = get_proxies()
            headers = dict()
            headers['User-Agent'] = get_user_agent()
            res = requests.get(url, headers=headers, timeout=60)
            res.encoding = "utf-8"
            if res.status_code == 200:
                return res.text
        except BaseException as e:
            print(e)


def parse_one_page(html):
    re_str = '<dd>.*?board-index.*?>(.*?)</i>.*?<img data-src="(.*?)".*?name.*?<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?' \
             'releasetime.*?>(.*?)</p>.*?score.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
    pattern = re.compile(re_str, re.S)
    items = re.findall(pattern, html)
    if items is None:
        return {}
    else:
        for item in items:
            # yield 生成器, 会返回一个迭代器对象
            yield {
                'index': item[0],
                'image_url': item[1],
                'name': item[2].strip(),
                'actor': item[3].strip().strip("主演："),
                'time': item[4].strip().strip("上映时间："),
                'score': eval(item[5].strip() + item[6].strip())
            }
    # print(items)


def parse_one_page2(html):
    parser = etree.HTMLParser(encoding="utf-8")
    text = etree.HTML(html, parser=parser)
    contents = text.xpath('//dd')
    index, image_url, name, star, release_time, integer, fraction = [], [], [], [], [], [], []

    for content in contents:
        # print(etree.tostring(content, encoding='utf-8').decode('utf-8'))
        # index, image_url, name, star, release_time, score是列表， 数据会一行行加进去
        index = content.xpath('//dd/i[contains(@class, "board-index")]/text()')
        image_url = content.xpath('//dd/a/img[@class="board-img"]/@data-src')
        name = content.xpath('//dd/div//p[@class="name"]/a/text()')
        star = content.xpath('//dd/div//p[@class="star"]/text()')
        release_time = content.xpath('//dd/div//p[@class="releasetime"]/text()')
        integer = content.xpath('//dd//div[contains(@class, "score-num")]//i[@class="integer"]/text()')
        fraction = content.xpath('//dd//div[contains(@class, "score-num")]//i[@class="fraction"]/text()')

    for item in range(len(index)):
        yield {
                "index": eval(str(index[item])),
                "image_url": str(image_url[item]),
                "name": str(name[item]),
                "star": str(star[item]).strip().strip("主演："),
                "release_time": str(release_time[item]).strip("上映时间："),
                "score": float(str(integer[item]) + str(fraction[item]))
        }


def parse_one_page3(html):
    soup = BeautifulSoup(html, "lxml")
    dds = soup.find_all(name='dd')
    for dd in dds:
        index = dd.find(name='i', attrs={'class': 'board-index'}).string
        image_url = dd.select('.image-link .board-img')[0]['data-src']
        name = dd.find(name='p', attrs={'class': 'name'}).string
        star = dd.find(name='p', attrs={'class': 'star'}).string.strip()
        releasetime = dd.find(name='p', attrs={'class': 'releasetime'}).string
        integer = dd.find(name='i', attrs={'class': 'integer'}).string
        fraction = dd.find(name='i', attrs={'class': 'fraction'}).get_text()
        yield {
            "index": index,
            "image_url": image_url,
            "name": name,
            "star": star.strip("主演："),
            "releasetime": releasetime.strip("上映时间："),
            "score": eval(integer+fraction)
        }


def write_to_file(content):
    # a 表示向文件追加，不会覆盖
    # filename = 'result' + time.strftime("_%Y_%m_%d_%H_%M_%S", time.gmtime()) + ".txt"
    with open('result.txt', 'a', encoding="utf-8") as f:
        # print(type(json.dumps(content)))
        f.writelines(json.dumps(content, ensure_ascii=False) + "\n")
    f.close()


def write_to_excel(content):
    app = xw.App(visible=True)
    app.display_alerts = False
    app.screen_updating = False
    # wb = app.books.add()
    wb = app.books.open("result.xlsx")
    ws = wb.sheets['sheet1']
    rg = ws.range('A1').expand()
    rows = rg.rows.count
    print(rows)
    if rows <= 1:
        ws.range('A' + str(rows)).value = content
    else:
        ws.range('A' + str(rows + 1)).value = content[1:]
    rg = ws.range('A1').expand()
    rg.columns.autofit()
    wb.save()
    wb.close()
    app.quit()
    pass


def to_list(content):
    lists = []
    # lst = []
    # add the titles
    # cont = next(content)  # next(content)不能写在下面for循环中，可能会出现异常, 迭代器只能往前不会后退。
    # for key in cont.keys():
    #     lst.append(key)
    # lists.append(lst)
    for item in content:
        lst = []
        if len(lists) == 0:
            for key in item.keys():
                lst.append(key)
            lists.append(lst)
            lst = []
        for value in item.values():
            lst.append(value)
        lists.append(lst)
    print(lists)
    return lists


def main(offset=0):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    text = parse_one_page3(html)
    for item in text:
        print(item)
        write_to_file(item)


if __name__ == "__main__":
    for i in range(10):
        main(i * 10)
        print("已完成：" + str((i + 1) / 10 * 100) + "%")
        if i >= 9:
            break
        time.sleep(random.randint(5, 10))
