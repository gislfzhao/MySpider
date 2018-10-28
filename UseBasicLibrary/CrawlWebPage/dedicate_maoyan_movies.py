# -*- coding: utf-8 -*-
import json
import re
import time
import requests
import xlwings as xw
import random


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers)
        # res.encoding = "utf-8"
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.exceptions as e:
        print(e)
        return None


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
    dict_iter = parse_one_page(html)
    # for item in dict_iter:
    #     print(item)
    #     write_to_file(item)
    write_to_excel(to_list(dict_iter))
    # print(html)


if __name__ == "__main__":
    for i in range(10):
        main(10 * i)
        time.sleep(random.randint(1, 3))
